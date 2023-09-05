let add_input = document.querySelector("#add")
let task_control = document.querySelector(".task-control")

add_input.addEventListener("click", () => {
    if(add_input.checked){
        task_control.classList.add("task-active")
    }else{
        task_control.classList.remove("task-active")
    }
});
