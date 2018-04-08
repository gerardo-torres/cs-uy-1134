function addElement(){

	var todo_list_node = $(".todo-list");
	var new_todo = $(".add-title").val();

	if (new_todo == "") {
		alert("Please enter a to-do item.");
		return;
	}

	var todo_list = JSON.parse(localStorage.getItem("todo"));

	if (todo_list == null) {
		todo_list = [];
	}

	todo_list.push([new_todo,false]);
	localStorage.setItem("todo",JSON.stringify(todo_list));

	todo_list_node.append(createTodoElement([new_todo,false],todo_list.length-1));

	$(".add-title").val('');

}

function removeElement(index) {
	$(".todo-item")[index].remove();
	var todo_list = JSON.parse(localStorage.getItem("todo"));
	todo_list.splice(index,1);
	localStorage.setItem("todo",JSON.stringify(todo_list));
	$.each($(".todo-item"),function(i, node){
		$(node).attr("data-index",i);
	});
}

function changeElement(index, status) {
	var todo_list = JSON.parse(localStorage.getItem("todo"));
	console.log(todo_list, index);
	todo_list[index][1] = status;
	localStorage.setItem("todo",JSON.stringify(todo_list));
	if (status) {
		$($(".todo-item")[index]).children("label").css("text-decoration","line-through");
	}else{
		$($(".todo-item")[index]).children("label").css("text-decoration","none");
	}
}

function populatePage() {
	var todo_list = JSON.parse(localStorage.getItem("todo"));
	var todo_list_node = $(".todo-list");
	if (todo_list != null) {
		$(".no-items-alert").remove();
		for (i = 0; i < todo_list.length; i++) {
			var curr_todo = todo_list[i];
			todo_list_node.append(createTodoElement(curr_todo,i));
		}
	}
}

function createTodoElement(todo,index) {
	var label_id = Math.floor(Math.random()*100000);
	var new_todo_node = $("<a href='#!'></a>")
	.addClass("todo-item collection-item")
	.attr("data-index",index)
	.append($("<label>")
		.attr("for","check"+label_id)
		.css("color", "#00695c")
		.text(todo[0]));
	var check = $("<input type='checkbox'/>")
	.attr("id","check"+label_id)
	.addClass("filled-in");
	if (todo[1]) {
		check.attr("checked","");
		new_todo_node.children("label").css("text-decoration","line-through");
	}
	check.change(function() {
		var i = parseInt($(this).parent().attr("data-index"));
	    changeElement(i,this.checked);
	})
	var cross = $("<a href='#!'></a>")
	.addClass("secondary-content")
	.append($("<i><i/>").addClass("material-icons").text("close	"));
	cross.click(function(){
		var i = parseInt($(this).parent().attr("data-index"));
		removeElement(i);
	});
	new_todo_node.prepend(check);
	new_todo_node.append(cross);
	return new_todo_node;
}

$(document).ready(function() {
	populatePage();
	document.querySelector(".add-title").addEventListener("keyup", event => {
		if(event.key !== "Enter") return;
		document.querySelector(".add-button").click();
		event.preventDefault();
	});
	$(".add-title").on("input", function () {
		if ($(this).val() == "") {
			$(".add-button").addClass("disabled");
		}else{
			$(".add-button").removeClass("disabled");
		}
	});

	$(".add-button").click(function () {
		$(this).addClass("disabled");
	});
});