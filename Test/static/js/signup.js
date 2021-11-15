function appendYear(){
	var date = new Date();
	var year = date.getFullYear();
	var selectValue = document.getElementById("year");
	var optionIndex = 0;

	for(var i=year-100;i<=year;i++){
			selectValue.add(new Option(i+"년",i),optionIndex++);
	}
}

function appendMonth(){
	var selectValue = document.getElementById("month"); 
	var optionIndex = 0;

	for(var i=1;i<=12;i++){
			selectValue.add(new Option(i+"월",i),optionIndex++);
	}
}

function appendDay(){
	var selectValue = document.getElementById("day");
	var optionIndex = 0;

	for(var i=1;i<=31;i++){
			selectValue.add(new Option(i+"일",i),optionIndex++);
	}
}
