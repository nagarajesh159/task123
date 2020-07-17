
window.onload=initAll;

var saveBookButton;
function initAll(){
    saveBookButton=document.getElementById('save_book');
    saveBookButton.onclick = saveBook
}

function saveBook(){
    var name = document.getElementById('book_name').value;
    var price = document.getElementById('book_price').value;
    var pages = document.getElementById('book_pages').value;
    var url = "/books/save_book?name="+name+"&price="+price+"&pages="+pages;
    var req = new XMLHttpRequest();
    alert(url)
    req.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var data = eval(req.responseText)
            alert(data)

        }
    };
    req.open('GET',url, true);
    req.send();
    alert('saved')
}

function showAllBooks(){
    var req = new XMLHttpRequest();
    url = "/books/getAllBooks"
    req.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var data = eval(req.responseText)
            alert(data)
            alert(data[0])
            var table = document.createElement('TABLE');
            var row = table.insertRow(0);
            var name = row.insertCell(0);
            var price = row.insertCell(1);
            var pages = row.insertCell(2);

            name.innerHTML="Book Name";
            price.innerHTML="Book Price";
            pages.innerHTML="No of Pages";
            var div = document.getElementById('bookslist')
            div.innerHTML=""

            for(var i=0; i<data.length; i++){
                var row = table.insertRow(i+1);
                var name = row.insertCell(0);
                var price = row.insertCell(1);
                var pages = row.insertCell(2);

                name.innerHTML=data[i].name;
                price.innerHTML=data[i].price;
                pages.innerHTML=data[i].pages;
            };
            table.className = 'table text-center table-striped'
            div.appendChild(table);
        }
    };
    req.open('GET', url, true);
    req.send();
};