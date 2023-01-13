class ColabGUIButton{
    constructor(key, font_color = "black", bg_color = "white", label = "Push"){
        const main = document.getElementById('colab_gui_main');
        this.elem = document.createElement('div');
        this.btn = document.createElement('div');
        this.elem.classList.add('colab_gui');
        this.btn.classList.add('btn');
        this.btn.classList.add('font_' + font_color);
        this.btn.classList.add('bg_' + bg_color);
        this.font_color = font_color;
        this.bg_color = bg_color;
        this.elem.setAttribute('id', key);
        main.appendChild(this.elem);
        this.elem.appendChild(this.btn);
        this.btn.innerHTML = label;
        this.click_events = {};
    }

    setClickEvent(function_name, ...args){
        const func = function(function_name, ...args){
            google.colab.kernel.invokeFunction(function_name, ...args);
        }
        this.btn.addEventListener('click', func, false);
        this.click_events[function_name] = func;
    }

    removeClickEvent(function_name){
        this.btn.removeEventListener('click', this.click_events[function_name]);
        this.click_events[function_name] = null;
    }
}

