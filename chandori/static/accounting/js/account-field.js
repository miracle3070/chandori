// ===============================================
// 달력 출력 관련

let date = new Date();

const renderCalendar = () => {
    // 이번 년도, 월 불러오기
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    // 달력 화면에 년, 월 출력
    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

    // 저번달, 이번달의 마지막 날짜의 요일과 일수를 불러옴
    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();


    // 달력에 표시할 저번달, 이번달, 다음달 날짜 구하기
    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];

    if (PLDay !== 6){
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }


    // 달력 날짜를 HTML에 출력
    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);
    dates.forEach((date, i) => {
        const condition = (i >= firstDateIndex) && (i < lastDateIndex + 1) ? 'this' : 'other';
        if (condition === 'this')
        {
            const dateString = viewYear.toString() + '-' + (viewMonth + 1).toString().padStart(2, '0') + '-' + date.toString().padStart(2, '0');
            dates[i] = `
            
            <div class="date" id="date${date}" onclick="setAccountFieldDate(date.getFullYear(), date.getMonth() + 1, ${date});">
            <a href="./${dateString}">
            <span class="${condition}">${date}</span>
            <div id="income${date}" class="income">아무 날짜나</div>
            <div id="expense${date}" class="expense">클릭해주세요.</div>
            </a>
            </div>
            `;
        }
        else
            dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`;
    })

    document.querySelector('.dates').innerHTML = dates.join('');


    // 오늘 날짜 그리기
    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.this')){
            if (+date.innerText === today.getDate()) {
                date.classList.add('today');
                break;
            }
        }
    }
}

const modifyCalendar = (inputDate) => {
    date = new Date(inputDate);

    // 이번 년도, 월 불러오기
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    // 달력 화면에 년, 월 출력
    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

    // 저번달, 이번달의 마지막 날짜의 요일과 일수를 불러옴
    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();


    // 달력에 표시할 저번달, 이번달, 다음달 날짜 구하기
    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];

    if (PLDay !== 6){
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }


    // 달력 날짜를 HTML에 출력
    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);
    dates.forEach((date, i) => {
        const condition = (i >= firstDateIndex) && (i < lastDateIndex + 1) ? 'this' : 'other';
        if (condition === 'this')
        {
            const dateString = viewYear.toString() + '-' + (viewMonth + 1).toString().padStart(2, '0') + '-' + date.toString().padStart(2, '0');
            dates[i] = `
            
            <div class="date" id="date${date}" onclick="setAccountFieldDate(date.getFullYear(), date.getMonth() + 1, ${date});">
            <a href="./${dateString}">
            <span class="${condition}">${date}</span>
            <div id="income${date}" class="income">수입: 15000</div>
            <div id="expense${date}" class="expense">지출: 8000</div>
            </a>
            </div>
            `;
        }
        else
            dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`;
    })

    document.querySelector('.dates').innerHTML = dates.join('');


    // 오늘 날짜 그리기
    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.this')){
            if (+date.innerText === today.getDate()) {
                date.classList.add('today');
                break;
            }
        }
    }
}


// 달력 그리는 함수 호출
renderCalendar();

const prevMonth = () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
}

const nextMonth = () => {
    date.setMonth(date.getMonth() + 1);
    renderCalendar();
}

const goToday = () => {
    date = new Date();
    renderCalendar();
}


// ===============================================
// 가계부 입력 관련

const removeAccountField = (number) => {
    const field = document.getElementById('field-list' + number);
    field.remove();
}


// 달력에 숫자를 누르면 폼 태그의 날짜가 변경
const setAccountFieldDate = (year, month, date) => {
    const dateString = year + '-' + month.toString().padStart(2, '0') + '-' + date.toString().padStart(2, '0');
    document.getElementById('account-date').setAttribute('value', dateString);
}

// 현재 날짜로 폼태그 설정
setAccountFieldDate(date.getFullYear(), date.getMonth()+1, date.getDate());
