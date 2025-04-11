# Test conditional statements
Team() {
    Feint @number = 10;  

    # Check even or odd
    Dribble (@number % 2 == 0) {
        Announce("The number " & @number & " is even.");
    } Shoot {
        Announce("The number " & @number & " is odd.");
    }
}

# Test with odd number
Team() {
    Feint @number = 11;  

    # Check even or odd
    Dribble (@number % 2 == 0) {
        Announce("The number " & @number & " is even.");
    } Shoot {
        Announce("The number " & @number & " is odd.");
    }
}

# Test with multiple conditions
Team() {
    Feint @score = 85;  

    Dribble (@score >= 90) {
        Announce("Grade: A");
    } Pass (@score >= 80) {
        Announce("Grade: B");
    } Pass (@score >= 70) {
        Announce("Grade: C");
    } Pass (@score >= 60) {
        Announce("Grade: D");
    } Shoot {
        Announce("Grade: F");
    }
} 