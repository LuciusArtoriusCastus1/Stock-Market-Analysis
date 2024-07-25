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
        link.classList.toggle('active', name === currentCategory);
        link.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelectorAll('#navbar a').forEach(a => a.classList.remove('active'));
            link.classList.add('active');
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

    for (let i = 1; i <= 60; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        button.classList.toggle('active', i === currentPage);
        button.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelectorAll('#pagination button').forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
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
    const labels = ['Rank', 'Name', label, 'Price', 'Today', 'Country']
    const row = document.createElement('tr');
    row.innerHTML = `
        <th>${labels[0]}</th>
        <th>${labels[1]}</th>
        <th>${labels[2]}</th>
        <th>${labels[3]}</th>
        <th>${labels[4]}</th>
        <th>${labels[5]}</th>
    `;
    tableHead.appendChild(row);
    data.forEach(item => {
        const row = document.createElement('tr');
        const todayValue = item['Refined Today']
        const todayClass = todayValue > 0 ? 'positive' : 'negative';
        row.innerHTML = `
            <td>${item.Rank}</td>
            <td>${item.Name}</td>
            <td>${item[label]}</td>
            <td>${item.Price}</td>
            <td class="${todayClass}">${item.Today}</td>
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
        img.src = `/images/${src}`;
        console.log();
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
    fetchData();
}

init();
