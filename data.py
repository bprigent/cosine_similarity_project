def get_text_pairs():
    """
    Returns a list of (category, AI generated text, Human reference text) tuples.
    Categories are: "rational", "suggestion", "issue detected", "confidence level"
    """
    return [
        # Rational explanations
        ("rational", "The process failed because the input data was corrupted.",
         "The error occurred due to invalid input data format."),
        
        ("rational", "The system is slow because of high memory usage.",
         "Performance issues are caused by excessive memory consumption."),
        
        ("rational", "The API returns 404 because the resource doesn't exist.",
         "The requested endpoint cannot be found on the server."),
        
        ("rational", "The code crashes due to a null pointer exception.",
         "The application fails when trying to access an undefined reference."),
        
        # Suggestions
        ("suggestion", "Try implementing a cache to improve performance.",
         "Adding a caching layer would make it faster."),
        
        ("suggestion", "Consider using async functions for better scalability.",
         "Implementation of asynchronous operations would enhance scaling."),
        
        ("suggestion", "You should add error handling for edge cases.",
         "It would be better to include exception handling for unexpected scenarios."),
        
        ("suggestion", "Consider breaking this function into smaller components.",
         "This method could be split into more manageable pieces."),
        
        # Issue detection
        ("issue detected", "There's a memory leak in the image processing module.",
         "The image processor is not properly releasing allocated memory."),
        
        ("issue detected", "The database connection times out after heavy load.",
         "Under stress, the DB connection fails to maintain stability."),
        
        ("issue detected", "The API authentication token expires too quickly.",
         "Security tokens are invalidated before completing the request cycle."),
        
        ("issue detected", "The user input validation is bypassed in some cases.",
         "Some edge cases allow invalid data to pass through the validation."),
        
        # Confidence levels
        ("confidence level", "I am 90% certain this is the root cause.",
         "There is high confidence that this is the source of the problem."),
        
        ("confidence level", "This solution will very likely resolve the issue.",
         "I'm quite confident this approach will fix the problem."),
        
        ("confidence level", "I'm not entirely sure, but this might help.",
         "This could potentially be a solution, but I'm not certain."),
        
        ("confidence level", "Based on the logs, I'm confident this is the bug.",
         "The log analysis strongly indicates this is the defect.")
    ]
