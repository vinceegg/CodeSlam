Team() {
    Feint @number = 10;  

    # Check even or odd
    Dribble (@number % 2 == 0) {
        Announce("The number " & @number & " is even.");
    } Shoot {
        Announce("The number " & @number & " is odd.");
    }
} 