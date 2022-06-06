// Price slider

const rangeInput = document.querySelectorAll(".range-input input"),
    priceInput = document.querySelectorAll(".price-input input"),
    range = document.querySelector(".price-slider .progress");
let priceGap = 250;

priceInput.forEach(input => {
    input.addEventListener("input", e => {
        let minPrice = parseInt(priceInput[0].value),
            maxPrice = parseInt(priceInput[1].value);

        if ((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max) {
            if (e.target.className === "input-min") {
                rangeInput[0].value = minPrice;
                range.style.left = ((minPrice / rangeInput[0].max) * 100) + "%";
            } else {
                rangeInput[1].value = maxPrice;
                range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
            }
        }
    });
});

rangeInput.forEach(input => {
    input.addEventListener("input", e => {
        let minVal = parseInt(rangeInput[0].value),
            maxVal = parseInt(rangeInput[1].value);

        if ((maxVal - minVal) < priceGap) {
            if (e.target.className === "range-min") {
                rangeInput[0].value = maxVal - priceGap
            } else {
                rangeInput[1].value = minVal + priceGap;
            }
        } else {
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            range.style.left = ((minVal / rangeInput[0].max) * 100) + "%";
            range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
        }
    });
});

// END Price slider


// Pagination 

// selecting required element
// const element = document.querySelector(".pagination ul");
// let totalPages = 2;
// let page = 10;
// //calling function with passing parameters and adding inside element which is ul tag
// element.innerHTML = createPagination(totalPages, page);
//
// function createPagination(totalPages, page) {
//     let liTag = '';
//     let active;
//     let beforePage = page - 1;
//     let afterPage = page + 1;
//     if (page > 1) { //show the next button if the page value is greater than 1
//         liTag += `<li class="btn prev" onclick="createPagination(totalPages, ${page - 1})"><span><i class="fas fa-angle-left"></i> Prev</span></li>`;
//     }
//     if (page > 2) { //if page value is less than 2 then add 1 after the previous button
//         liTag += `<li class="first numb" onclick="createPagination(totalPages, 1)"><span>1</span></li>`;
//         if (page > 3) { //if page value is greater than 3 then add this (...) after the first li or page
//             liTag += `<li class="dots"><span>...</span></li>`;
//         }
//     }
//     // how many pages or li show before the current li
//     if (page === totalPages) {
//         beforePage = beforePage - 2;
//     } else if (page === totalPages - 1) {
//         beforePage = beforePage - 1;
//     }
//     // how many pages or li show after the current li
//     if (page === 1) {
//         afterPage = afterPage + 2;
//     } else if (page === 2) {
//         afterPage = afterPage + 1;
//     }
//     for (var plength = beforePage; plength <= afterPage; plength++) {
//         if (plength > totalPages) { //if plength is greater than totalPage length then continue
//             continue;
//         }
//         if (plength === 0) { //if plength is 0 than add +1 in plength value
//             plength = plength + 1;
//         }
//         if (page === plength) { //if page is equal to plength than assign active string in the active variable
//             active = "active";
//         } else { //else leave empty to the active variable
//             active = "";
//         }
//         liTag += `<li class="numb ${active}" onclick="createPagination(totalPages, ${plength})"><span>${plength}</span></li>`;
//     }
//     if (page < totalPages - 1) { //if page value is less than totalPage value by -1 then show the last li or page
//         if (page < totalPages - 2) { //if page value is less than totalPage value by -2 then add this (...) before the last li or page
//             liTag += `<li class="dots"><span>...</span></li>`;
//         }
//         liTag += `<li class="last numb" onclick="createPagination(totalPages, ${totalPages})"><span>${totalPages}</span></li>`;
//     }
//     if (page < totalPages) { //show the next button if the page value is less than totalPage(20)
//         liTag += `<li class="btn next" onclick="createPagination(totalPages, ${page + 1})"><span>Next <i class="fas fa-angle-right"></i></span></li>`;
//     }
//     element.innerHTML = liTag; //add li tag inside ul tag
//     return liTag; //reurn the li tag
// }
// END Pagination

// Dopdown list

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

// END dropdown list

// START LIVE search

const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (product) => {
    $.ajax({
        type: 'POST',
        url: '/search/',
        data:{
            'csrfmiddlewaretoken' : csrf,
            'product' : product
        },
        success: (res) =>{
            const data = res.data
            if (Array.isArray(data)) {
                 resultBox.innerHTML = ""
                data.forEach(product=> {
                    resultBox.innerHTML += `<a href="${product.url}">\n
                            <div class="row mt-2 mb-2">
                                <div class="col-2">
                                    <img src="${product.img}" alt="">
                                </div>
                                <div class="col-8">
                                    <h5>${product.title}</h5>
                                </div>
                                <div class="col-8">
                                    <h5>${product.price} грн</h5>
                                </div>
                            </div>
                        </a>`
                 })
            }else {
                if (searchInput.value.length > 0){
                    resultBox.innerHTML = `<b>${data}</b>`
                }else{
                    resultBox.classList.add('not-visible')
                }
            }
        },
        error:(err)=>{
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup',e=>{

    if (resultBox.classList.contains('not-visible')) {
        resultBox.classList.remove('not-visible')
    }
    sendSearchData(e.target.value)
})

// END LIVE search