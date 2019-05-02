club_title <- c("Chess Club")
club_description <- c("Meets two nights a week for members to play chess. Snacks are provided.")
club_dues <- c(50, 20, 15)
meeting_days <- c("Monday", "Wednesday")
meeting_times <- c("6:00 pm", "8:00 pm")

club_meetings <- rbind(meeting_days, meeting_times)

chess_club <- list(club_title, club_description, club_dues, club_meetings)