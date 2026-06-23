document.addEventListener("DOMContentLoaded", () => {
    const reviewPopup = document.querySelector("#reviewPopup");
    const reviewClose = document.querySelector("#reviewClose");

    const attendancePopup = document.querySelector("#attendancePopup");
    const attendanceForm = document.querySelector("#attendanceForm");
    const deliveryArea = document.querySelector(".delivery-area");

    const shouldShowReview = reviewPopup?.dataset.showPopup === "true";
    const shouldShowAttendance = attendancePopup?.dataset.showPopup === "true";
    const todayDay = Number(attendancePopup?.dataset.todayDay || 0);
    const attendedDays = (attendancePopup?.dataset.attendanceDays || "")
        .split(",")
        .map((day) => Number(day))
        .filter(Boolean);

    function showPopup(popup) {
        popup?.classList.add("show");
        deliveryArea?.classList.add("blurred");
    }

    function hidePopup(popup) {
        popup?.classList.remove("show");

        if (!document.querySelector(".review-popup.show, .attendance-popup.show")) {
            deliveryArea?.classList.remove("blurred");
        }
    }

    document.querySelectorAll(".attendance-item").forEach((item) => {
        const day = Number(item.dataset.day);
        const isCompleted = attendedDays.includes(day);
        const isToday = day === todayDay;

        item.classList.toggle("completed", isCompleted);
        item.classList.toggle("today", isToday && !isCompleted);
        item.classList.toggle("disabled", !isToday || isCompleted);
    });

    if (shouldShowReview) {
        showPopup(reviewPopup);
    } else if (shouldShowAttendance) {
        showPopup(attendancePopup);
    }

    attendanceForm?.addEventListener("submit", () => {
        const todayItem = document.querySelector(`.attendance-item[data-day="${todayDay}"]`);
        todayItem?.classList.add("completed");
    });

    reviewClose?.addEventListener("click", () => {
        hidePopup(reviewPopup);

        if (shouldShowAttendance) {
            showPopup(attendancePopup);
        }
    });
});
