document.addEventListener('DOMContentLoaded', function () {
    const divisionSelect = document.getElementById('id_division');
    const districtSelect = document.getElementById('id_district');

    if (divisionSelect && districtSelect) {
        // Trigger AJAX when division changes
        divisionSelect.addEventListener('change', function () {
            const divisionId = this.value;

            // Clear district dropdown if no division selected
            if (!divisionId) {
                districtSelect.innerHTML = '';
                return;
            }

            fetch(`/admin/yourapp/person/get_districts/?division=${divisionId}`)
                .then(response => response.json())
                .then(data => {
                    districtSelect.innerHTML = '';
                    data.forEach(district => {
                        const option = document.createElement('option');
                        option.value = district.id;
                        option.text = district.district_name;
                        districtSelect.appendChild(option);
                    });
                });
        });

        // Trigger change event on page load to populate districts for edit form
        if (divisionSelect.value) {
            const event = new Event('change');
            divisionSelect.dispatchEvent(event);
        }
    }
});
