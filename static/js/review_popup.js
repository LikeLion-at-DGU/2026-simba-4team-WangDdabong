const reviewPopup = document.querySelector("#reviewPopup");
const reviewClose = document.querySelector("#reviewClose");

const attendancePopup = document.querySelector("#attendancePopup");
const attendanceClose = document.querySelector("#attendanceClose");

const deliveryArea = document.querySelector(".delivery-area");

// 임시 테스트용
// 나중에 백엔드에서 하루 1회 여부를 내려주면 이 값만 바꾸면 됨
const hasNewReview = true;
const shouldShowAttendance = true;

function blurDeliveryArea() {
    if (deliveryArea) {
        deliveryArea.classList.add("blurred");
    }
}

function unblurDeliveryArea() {
    if (deliveryArea) {
        deliveryArea.classList.remove("blurred");
    }
}

function openReviewPopup() {
    if (reviewPopup) {
        reviewPopup.classList.add("active");
        blurDeliveryArea();
    }
}

function closeReviewPopup() {
    if (reviewPopup) {
        reviewPopup.classList.remove("active");
    }
}

function openAttendancePopup() {
    if (attendancePopup) {
        attendancePopup.classList.add("active");
        blurDeliveryArea();
    }
}

function closeAttendancePopup() {
    if (attendancePopup) {
        attendancePopup.classList.remove("active");
        unblurDeliveryArea();
    }
}

// 홈 들어오면 후일담 팝업 먼저 자동 표시
if (hasNewReview) {
    openReviewPopup();
} else if (shouldShowAttendance) {
    openAttendancePopup();
}

// 후일담 X 누르면 후일담 닫고 출석체크 열기
if (reviewClose) {
    reviewClose.addEventListener("click", () => {
        closeReviewPopup();

        if (shouldShowAttendance) {
            openAttendancePopup();
        } else {
            unblurDeliveryArea();
        }
    });
}

// 출석체크 X 누르면 출석체크 닫고 양 다시 선명하게
if (attendanceClose) {
    attendanceClose.addEventListener("click", () => {
        closeAttendancePopup();
    });
}