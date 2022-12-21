function createButton(temp_id){
    const elem = document.createElement('div');
    elem.classList.add('colab_gui');
    elem.setAttribute('id', temp_id);
    const btn = document.createElement('div');

}
class ColabGUIBtn{
    constructor(key, label){
        this.elem = document.createElement('div');
        this.btn = document.createElement('div');
        this.elem.classList.add('colab_gui');
        this.elem.setAttribute('id', key);
        this.events = {};
    }

    setEvent(function_name, ...args){
        const func = this.btn.addEventListener('click', function(){
            google.colab.kernel.invokeFunction(function_name, ...args);
        }, false);
        this.events[function_name] = func;
    }

    removeEvent(function_name){
        this.elem.removeEventListener('click', this.events[function_name]);
        this.events[function_name] = null; 
    }
}