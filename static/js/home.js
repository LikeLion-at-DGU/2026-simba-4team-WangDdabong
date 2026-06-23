document.addEventListener("DOMContentLoaded", () => {
    const reviewPopup = document.querySelector("#reviewPopup");
    const reviewClose = document.querySelector("#reviewClose");

    const attendancePopup = document.querySelector("#attendancePopup");
    const attendanceClose = document.querySelector("#attendanceClose");

    // 테스트용: 현재 출석할 차례
    // DAY 1 테스트면 1, DAY 3 테스트면 3으로 바꾸면 됨
    let currentAttendanceDay = 1;

    // 새로고침할 때마다 출첵 팝업 무조건 띄우기
    attendancePopup?.classList.add("show");

    // 현재 차례 이전 DAY들은 처음부터 흐리게 처리
    document.querySelectorAll(".attendance-item").forEach((item) => {
        const day = Number(item.dataset.day);

        if (day < currentAttendanceDay) {
            item.classList.add("completed");
        }
    });

    // DAY 아이템 누르면 현재 차례 DAY만 즉시 흐리게
    document.querySelectorAll(".attendance-item").forEach((item) => {
        const day = Number(item.dataset.day);

        item.addEventListener("click", () => {
            if (day === currentAttendanceDay) {
                item.classList.add("completed");
                currentAttendanceDay += 1;
            }
        });
    });

    // 출석체크 하기 누르면 출첵 팝업 닫고 후일담 팝업 열기
    attendanceClose?.addEventListener("click", () => {
        attendancePopup?.classList.remove("show");
        reviewPopup?.classList.add("show");
    });

    // 후일담 팝업 닫기
    reviewClose?.addEventListener("click", () => {
        reviewPopup?.classList.remove("show");
    });
});