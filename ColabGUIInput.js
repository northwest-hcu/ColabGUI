class ColabGUIInput{
    constructor(key, label){
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
        // this.content.value = 'test content';
        this.key = key;
    }
    getValue(){
        return this.content.value;
    }
    setLabel(label){
        this.label.innerHTML = label;
    }
}