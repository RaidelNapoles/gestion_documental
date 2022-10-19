$(document).ready(function () {
	$("#example").DataTable({
		select: true,
		lengthMenu: [
			[-1, 5, 10, 20, 30, 40, 50],
			["Todos", 5, 10, 20, 30, 40, 50],
		],
		language: {
			decimal: "",
			emptyTable: "No hay datos diponibles",
			info: "Mostrando del _START_ al _END_ de _TOTAL_ registros",
			infoEmpty: "0 a 0 de 0 registros",
			infoFiltered: "(filtrados de un total de _MAX_ registros)",
			infoPostFix: "",
			thousands: "",
			lengthMenu: "Mostrar _MENU_ registros",
			loadingRecords: "Cargando...",
			processing: "Procesando...",
			search: "Buscar:",
			zeroRecords: "Ningún registro coincidió",
			paginate: {
				first: "Primero",
				last: "Último",
				next: "Siguiente",
				previous: "Anterior",
			},
			aria: {
				sortAscending:
					": activa para ordenar ascendentemente por la columna",
				sortDescending:
					": activa para ordenar descendentemente por la columna",
			},
		},
	});
});
