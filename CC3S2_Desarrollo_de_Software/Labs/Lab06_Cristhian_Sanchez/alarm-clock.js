var ac = {
	// (A) INICIALIZAMOS EL RELOJ
	init: function() {
		// (A1) OBTENEMOS LA HORA ACTUAL - HOUR, MIN, SEG
		ac.chr = document.getElementById('chr');
		ac.cmin = document.getElementById('cmin');
		ac.csec = document.getElementById('csec');

		// (A2) CREAMOS EL SELECTOR DE TIEMPO - HR, MIN, SEG
		ac.thr = ac.createSel(23);
		document.getElementById('tpick-h').appendChild(ac.thr);
		ac.thm = ac.createSel(59);
		document.getElementById('tpick-m').appendChild(ac.thm);
		ac.ths = ac.createSel(59);
		document.getElementById('tpick-s').appendChild(ac.ths);

		// (A3) CREAMOS EL SELECTOR DE TIEMPO - ESTABLECER, RESETEAR
		ac.tset = document.getElementById('tset');
		ac.tset.addEventListener('click', ac.set);
		ac.treset = document.getElementById('treset');
		ac.treset.addEventListener('click', ac.reset);

		// (A4) OBTENER EL SONIDO DE ALARMA
		ac.sound = document.getElementById('alarm-sound');

		// (A5) INICIAR EL RELOJ
		ac.alarm = null;
		setInterval(ac.tick, 1000);
	},

	// (B) SELECTOR PARA HR, MIN, SEG
	createSel: function(max) {
		var selector = document.createElement('select');
		for (var i = 0; i <= max; i++) {
			var opt = document.createElement('option');
			i = ac.padzero(i);
			opt.value = i;
			opt.innerHTML = i;
			selector.appendChild(opt);
		}
		return selector;
	},

	// (C) IMPRIMIR HR, MIN, SEG CON UN 0 (SI SON < 10)
	padzero: function(num) {
		if (num < 10) {
			num = '0' + num;
		} else {
			num = num.toString();
		}
		return num;
	},

	// (D) ACTUALIZAR HORA ACTUAL
	tick: function() {
		// (D1) HORA ACTUAL
		var now = new Date();
		var hr = ac.padzero(now.getHours());
		var min = ac.padzero(now.getMinutes());
		var sec = ac.padzero(now.getSeconds());

		// (D2) ACTUALIZAR EL RELOJ
		ac.chr.innerHTML = hr;
		ac.cmin.innerHTML = min;
		ac.csec.innerHTML = sec;

		// (D3) VERIFICAR Y HACER SONAR ALARMA
		if (ac.alarm != null) {
			now = hr + min + sec;
			if (now == ac.alarm) {
				if (ac.sound.paused) {
                    alert('Alarma activada!');
					ac.sound.play();
				}
			}
		}
	},

	// (E) ESTABLECER LA ALARMA
	set: function() {
		ac.alarm = ac.thr.value + ac.thm.value + ac.ths.value;
		ac.thr.disabled = true;
		ac.thm.disabled = true;
		ac.ths.disabled = true;
		ac.tset.disabled = true;
		ac.treset.disabled = false;
	},

	// (F) RESETEAR LA ALARMA
	reset: function() {
		if (!ac.sound.paused) {
			ac.sound.pause();
		}
		ac.alarm = null;
		ac.thr.disabled = false;
		ac.thm.disabled = false;
		ac.ths.disabled = false;
		ac.tset.disabled = false;
		ac.treset.disabled = true;
	}
};
// (G) INICIAR LA APLICACIÓN CUANDO SE CARGA LA PÁGINA
window.addEventListener('load', ac.init);
