/**
 * Created by diogo on 25/06/17.
 */

function delete_category(cid, name) {

    document.getElementById('confirmation_text').innerHTML = 'Do you confirm' +
        ' the removal of category <b><i>' +
        name + '</i></b>?';

    var deleteFormWrapper = function(){
        deleteForm('/category/' + cid + '/delete');
    };

    document.getElementById('operation_btn').addEventListener('click', deleteFormWrapper);


}

function delete_game(gid, name) {

    document.getElementById('confirmation_text').innerHTML = 'Do you confirm' +
        ' the removal of <b><i>' +
        name + '</i></b>?';

    var deleteFormWrapper = function(){
        deleteForm('/game/' + gid + '/delete');
    };

    document.getElementById('operation_btn').addEventListener('click', deleteFormWrapper);
}

var deleteForm = function (url) {
    var delForm = document.createElement('form');
    delForm.id = 'deletion_frm';
    delForm.method = 'post';
    delForm.action = url;
    document.body.appendChild(delForm);

    delForm.submit();
    document.body.removeChild(delForm);
};
