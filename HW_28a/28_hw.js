window.addEventListener('DOMContentLoaded', (event) => {
  const addFriendButton = document.getElementById('add-friend-btn');
  const messageButton = document.getElementById('message-btn');
  const friendCountElement = document.getElementById('count');
  const submitHomeworkButton = document.getElementById('submit-homework-btn');
  const homeworkTable = document.querySelector('.table tbody');

  const initialFriendCount = Math.floor(Math.random() * 100);
  friendCountElement.textContent = initialFriendCount;

  const addFriend = () => {
    const currentCount = parseInt(friendCountElement.textContent);
    const updatedCount = currentCount + 1;
    friendCountElement.textContent = updatedCount;

    addFriendButton.textContent = 'Очікується підтвердження';
    addFriendButton.disabled = true;
  };

  let isColorChanged = false;

  const changeButtonColor = () => {
    if (isColorChanged) {
      messageButton.style.color = '';
    } else {
      messageButton.style.color = 'red';
    }

    isColorChanged = !isColorChanged;
  };

  const submitHomework = () => {
    const newRow = document.createElement('tr');
    const homeworkNameCell = document.createElement('td');
    const homeworkGradeCell = document.createElement('td');

    homeworkNameCell.textContent = '№24 «Знайомство з html»';
    homeworkGradeCell.textContent = 'ДЗ надіслано';
    homeworkGradeCell.classList.add('submitted-homework');

    newRow.appendChild(homeworkNameCell);
    newRow.appendChild(homeworkGradeCell);
    homeworkTable.appendChild(newRow);
  };

  addFriendButton.addEventListener('click', addFriend);
  messageButton.addEventListener('click', changeButtonColor);
  submitHomeworkButton.addEventListener('click', submitHomework);
});
