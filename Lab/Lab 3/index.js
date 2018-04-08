function updateView() {
	$.ajax({
		method: "GET",
		url: "/todo/read",
		success: function (payload) {
			console.log(payload);
			var todo_list_node = $(".todo-list");
			$(".todo-item").remove();
			for (var i = 0; i < payload.data.length; i++) {
				var todo = payload.data[i];
				var todo_node = createTodoElement(todo,i);
				todo_list_node.append(todo_node);
			};
		}	
	});
}

function createTodo(title) {
	$.ajax({
		method: "POST",
		url: "/todo/create",
		contentType: "application/json",
		dataType: "json",
		data: JSON.stringify({
			content: title
		}),
		success: function (data) {
			console.log(data);
			$(".add-title").val('');
			updateView();
		}	
	});	
}

function updateTodo(index) {
	$.ajax({
		method: "PUT",
		url: "/todo/update",
		contentType: "application/json",
		dataType: "json",
		data: JSON.stringify({
			item_number: index
		}),
		success: function (data) {
			console.log(data);
			updateView();
		}	
	});	
}

function deleteTodo(index) {
	$.ajax({
		method: "DELETE",
		url: "/todo/delete",
		contentType: "application/json",
		dataType: "json",
		data: JSON.stringify({
			item: index
		}),
		success: function (data) {
			console.log(data);
			updateView();
		}	
	});	
}

function createTodoElement(todo,index) {
	var label_id = Math.floor(Math.random()*100000);
	var new_todo_node = $("<a href='#!'></a>")
	.addClass("todo-item collection-item")
	.attr("data-index",index)
	.append($("<label>")
		.attr("for","check"+label_id)
		.css("color", "#00695c")
		.text(todo.title));
	var check = $("<input type='checkbox'/>")
	.attr("id","check"+label_id)
	.addClass("filled-in");
	if (todo.done) {
		check.attr("checked","");
		new_todo_node.children("label").css("text-decoration","line-through");
	}
	check.change(function() {
		var i = parseInt($(this).parent().attr("data-index"));
	    updateTodo(i);
	})
	var cross = $("<a href='#!'></a>")
	.addClass("secondary-content")
	.append($("<i><i/>").addClass("material-icons").text("close	"));
	cross.click(function(){
		var i = parseInt($(this).parent().attr("data-index"));
		deleteTodo(i);
	});
	new_todo_node.prepend(check);
	new_todo_node.append(cross);
	return new_todo_node;
}

$(document).ready(function() {
	updateView();
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
		createTodo($(".add-title").val());
		$(this).addClass("disabled");
	});

});

