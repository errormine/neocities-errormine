var links = JSON.parse(webring);
var div = document.getElementById("webring-container");
var ul = document.createElement("ul");
div.appendChild(ul);

for (var i = 0; i < links.length; i++) {
    var website = links[i].website;
    if (website == document.location.origin) continue;
    var banner = links[i].banner;
    var pageName = links[i].name;
    var li = document.createElement("li");
    var a  = document.createElement("a");
    a.href = website;
    var img = document.createElement("img");
    img.width = 240;
    img.height = 60;
    img.src = banner;
    img.alt = pageName;
    
    ul.appendChild(li).appendChild(a).appendChild(img);
}