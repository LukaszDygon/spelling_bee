function delay(milliseconds){
    return new Promise(resolve => {
        setTimeout(resolve, milliseconds);
    });
}

async function enterWords(words) {
    for (i=0; i < words.length; i++) {
        console.log(i + ' writing ' + words[i]);
        await simulateWriting(words[i]);
        await delay(1000);
    }
}

async function simulateWriting(val) {
    for (c=0; c < val.length; c++) {
        window.dispatchEvent(new KeyboardEvent('keydown', {'key': val[c]}));
        await delay(200);
    }
    window.dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));
}

words = `>PLACEHOLDER<`.split('\n');

await enterWords(words);
