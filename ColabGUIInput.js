class ColabGUIInput{
    constructor(key, label = "Input > "){
        const main = document.getElementById('colab_gui_main');
        this.elem = document.createElement('div');
        this.label = document.createElement('div');
        this.content = document.createElement('input');
        this.elem.classList.add('colab_gui');
        this.label.classList.add('input_label');
        this.content.classList.add('input_text');
        this.content.type = 'text';
        this.elem.setAttribute('id', key);
        main.appendChild(this.elem);
        this.elem.appendChild(this.label);
        this.elem.appendChild(this.content);
        this.label.innerHTML = label;
        this.content.value = 'test content';
        this.key = key;
    }
    /*getValue(){
        google.colab.kernel.invokeFunction('n.testGetter', [this.key, this.content.value], {});
    }*/
}

function getValue(key){
    const values = document.querySelectorAll('.colab_gui .input_text');
    for(let i=0; i<values.length; i++){
        console.log(values[i]);
    }
    if(values[i].parentNode.id === key){
        return values[i];
    }
    return false;
}

async function getValueFunction(key){
    google.colab.kernel.invokeFunction('n.testGetter', [key, getValue(key)], {});
}