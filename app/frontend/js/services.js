const navbar = {
    'Market Cap': 'http://127.0.0.1:8000/market-cap/page/',
    'Earnings': 'http://127.0.0.1:8000/most-profitable-companies/page/',
    'Revenue': 'http://127.0.0.1:8000/largest-companies-by-revenue/page/',
    'Total assets': 'http://127.0.0.1:8000/top-companies-by-total-assets/page/',
    'Net assets': 'http://127.0.0.1:8000/top-companies-by-net-assets/page/',
    'Total liabilities': 'http://127.0.0.1:8000/companies-with-the-highest-liabilities/page/',
    'Total debt': 'http://127.0.0.1:8000/companies-with-the-highest-debt/page/',
    'Cash on hand': 'http://127.0.0.1:8000/companies-with-the-highest-cash-on-hand/page/'
};

let currentPage = 1;
let currentCategory = 'Market Cap';

function createNavbar() {
    const navElement = document.getElementById('navbar');
    for (const [name, url] of Object.entries(navbar)) {
        const link = document.createElement('a');
        link.href = '#';
        link.textContent = name;
        link.addEventListener('click', (e) => {
            e.preventDefault();
            currentCategory = name;
            currentPage = 1;
            fetchData();
        });
        navElement.appendChild(link);
    }
}

function createPagination() {
    const paginationElement = document.getElementById('pagination');
    paginationElement.innerHTML = '';

    for (let i = 1; i <= 88; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        button.addEventListener('click', (e) => {
            e.preventDefault()
            currentPage = i;
            fetchData();
        });
        paginationElement.appendChild(button);
    }
}

function updateTable(data, label) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';
    const tableHead = document.getElementById('tableHead');
    tableHead.innerHTML = '';
    const labels = ['Name', label, 'Price', 'Today', 'Country']
    const row = document.createElement('tr');
    row.innerHTML = `
        <th>${labels[0]}</th>
        <th>${labels[1]}</th>
        <th>${labels[2]}</th>
        <th>${labels[3]}</th>
        <th>${labels[4]}</th>
    `;
    tableHead.appendChild(row);
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.Name}</td>
            <td>${item[label]}</td>
            <td>${item.Price}</td>
            <td>${item.Today}</td>
            <td>${item.Country}</td>
        `;
        tableBody.appendChild(row);
    });
}

function displayImages(images) {
    const imagesElement = document.getElementById('images');
    imagesElement.innerHTML = '';

    images.forEach(src => {
        const img = document.createElement('img');
        img.src = "../../backend/images/" + src;
        img.alt = 'Financial Data Image';
        imagesElement.appendChild(img);
    });
}

async function fetchData() {
    const url = `${navbar[currentCategory]}${currentPage}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        updateTable(data.data, data.label);
        displayImages(data.images);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function init() {
    createNavbar();
    createPagination();
}

init();
