class ColabGUIRadio{
    constructor(key, labels, values){
        const main = document.getElementById('colab_gui_main');
        this.elem = document.createElement('div');
        this.elem.classList.add('colab_gui');
        this.elem.setAttribute('id', key);
        this.selectors = [];
        for(let i=0; i<labels.length; i++){
            let line = {"label":"", "value":""};
            let label_elem, value_elem, br_elem;
            label_elem = document.createElement('div');
            value_elem = document.createElement('input');
            br_elem = document.createElement('br');
            value_elem.type = "radio";
            value_elem.name = "colabguiradio_" + key;
            label_elem.classList.add('input_content_label');
            value_elem.classList.add('input_radio');
            label_elem.innerHTML = labels[i];
            value_elem.value = values[i];
            line.label = label_elem;
            line.value = value_elem;
            this.selectors.push(line);
            this.elem.appendChild(value_elem);
            this.elem.appendChild(label_elem);
            this.elem.appendChild(br_elem);
            if(i === 0){
                value_elem.checked = true;
            }
        }
        main.appendChild(this.elem);
        this.key = key;
    }
    getValue(){
        for(let i=0; i<this.selectors.length; i++){
            if(this.selectors[i].value.checked){
                return this.selectors[i].value.value;
            }
        }
        return false;
    }
}