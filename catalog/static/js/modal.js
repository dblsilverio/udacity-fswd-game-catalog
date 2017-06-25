/**
 * Created by diogo on 25/06/17.
 */

function delete_category(cid, name) {

    document.getElementById('confirmation_text').innerHTML = 'Do you confirm' +
        ' the removal of category <b><i>' +
        name + '</i></b>?';

    document.getElementById('operation_btn').addEventListener('click', function () {
        var delForm = document.createElement('form');
        delForm.id = 'category_deletion_frm';
        delForm.method = 'post';
        delForm.action = '/category/' + cid + '/delete';
        document.body.appendChild(delForm);

        delForm.submit();
        document.body.removeChild(delForm);
    });

}
