const $word = $('input[name="word"]')
const $form = $('.ans-form')
const $button = $('button')
const $timer = $('.timer')
const $score = $('.score')
let score = 0;
let time = 60;



const handleSubmit = async (e) => {
    e.preventDefault()
    word = e.target[0].value;

    try {
        res = await axios.post('/validate', {
            word: word
        })
        check = res.data.result;
        if (answerValidate(check)) {
            scoreGame(word);
            $score.text(`${score}`);
        }
    } catch (error) {
        console.log(error);
    }
}

const answerValidate = (ans) => {
    if (ans === 'ok') {
        alert('Word is found')
        return true
    } else if (ans === 'not-on-board') {
        alert('Word is not on board')
        return false
    }
    if (ans === 'not-word') {
        alert('Not a word')
        return false
    }
}

const scoreGame = (word) => {
    score += word.length
    return score
}

const gameTimer = () => {
    countdown = setInterval(() => {
        $timer.text(`${time}`)
        time--;
        if (time < 0) {
            clearInterval(countdown)
            $button.attr('disabled', true)
            alert('Game Over!')
            sendScore(score);
        }
    }, 1000)
}

const sendScore = async (scr) => {
    try {
        res = axios.post("/stats", {
            score: score
        })
        console.log(res);
    } catch (error) {
        console.log(error);
    }
}

gameTimer()

$form.on("submit", handleSubmit)