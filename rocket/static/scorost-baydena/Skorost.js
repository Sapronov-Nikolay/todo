var distance = [] // пустой массив для того, чтобы туда заносились введённые вычисления по дистанции
var times = [] // пустой массив для того, чтобы туда заносились введённые вычисления по по времени

function save() { // МОЗГОВЫЛАМЫВАЛКА ДЛЯ КНОПКИ "ВЫЧИСЛИТЬ"
    let my_time = new Date();
    let kilom = document.getElementById("distance");
    let tm = document.getElementById("time");
    let tbl = document.getElementById("record");
    tbl.innerHTML += '<tr><th>' + my_time + '</th>' + '<th>' + kilom.value + ' km</th>' + '<th>' + tm.value + ' мин.</th></tr>';

    distance.push(kilom.value);
    times.push(tm.value);

    document.getElementById("avgs").innerHTML = avg(distance, times);
}

function avg(rasst, vrem) { // МОЗГОВЫЛАМЫВАЛКА ДЛЯ ВЫЧИСЛЕНИЯ РЕЗУЛЬТАТА ДЛЯ БАЙДЕНА
    let sum = 0;
    let sum_t = 0;
    let nomer_elementa = 0;
    console.log('nomer_elementa = ' + nomer_elementa + '; Кол-во пробежек:' + rasst.length + '[' + rasst + ']');
    while (nomer_elementa < rasst.length) {
        sum += rasst[nomer_elementa];
        sum_t += vrem[nomer_elementa];
        nomer_elementa += 1;
        console.log('nomer_elementa=' + nomer_elementa + '; Кол-во пробежек:' + rasst.length + '[' + rasst + ']');

    }
    return sum / sum_t;
}