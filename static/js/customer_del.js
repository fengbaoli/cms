function fun(){
	var boxes = document.getElementsByName("customerinfo");
	for(i=0;i<boxes.length;i++){
		if(boxes[i].checked){
			tr = boxes[i].parentNode.parentNode;
			tr.parentNode.removeChild(tr);
		}
	}
}
