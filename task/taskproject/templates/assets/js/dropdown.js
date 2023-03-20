var date=[
["Honda,Civik"],
["Honda,Civik22"],
["hyundai,creta"]
];

const filtdropdown=data.filter(r=>r[0]==="Honda");

const uniq=new set();
filtdropdown.forEach(r=>uniq.add(r[1]));
const uniqlist=[...uniq];
const place=document.getElementById("place");

uniqlist.forEach(item =>{
    const option =document.createElement("option");
    option.textContent=item;
    place.appendChild(option);

})
