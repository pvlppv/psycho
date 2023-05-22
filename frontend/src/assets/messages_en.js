$(document).ready(function() {
    var messageInput = $('#hero-feed-send-input');
    var messageForm = $('#hero-feed-send');
    var messageFeed = $('#hero-feed-2');

    messageForm.on('submit', function(event) {
        event.preventDefault();
        var messageText = messageInput.val();
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                'message_text': messageText,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
                messageFeed.prepend('<div class="hero-feed-message">' + 
                    '<i class="hero-feed-message-pic bx bxs-user"></i>' + 
                    '<div class="hero-feed-message-text">' + 
                    '<div class="hero-feed-message-text-1">' + 
                    '<div class="hero-feed-message-text-1-username">Anonymous</div>' + 
                    '<div class="hero-feed-message-text-1-time">Just now</div>' + 
                    '</div>' + 
                    '<div class="hero-feed-message-text-2">' + 
                    messageText + 
                    '</div>' + 
                    '</div>' + 
                    '</div>');
                messageInput.val('');
            }
        });
    });
});
