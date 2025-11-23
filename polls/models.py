from django.db import models
from django.utils import timezone


class Poll(models.Model):
    """
    Represents a poll with a question and multiple choices.
    Each poll has a title, question text, and can be active or past.
    """
    title = models.CharField(max_length=200)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        """Returns the poll title for display"""
        return self.title
    
    def is_currently_active(self):
        """
        Checks if poll is currently active based on end_date.
        Returns True if poll is active and hasn't ended yet.
        """
        if not self.is_active:
            return False
        if self.end_date and timezone.now() > self.end_date:
            return False
        return True
    
    def get_total_votes(self):
        """Returns the total number of votes for this poll"""
        total = 0
        for choice in self.choice_set.all():
            total += choice.votes
        return total


class Choice(models.Model):
    """
    Represents a choice option within a poll.
    Each choice belongs to a poll and has a text option and vote count.
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """Returns the choice text for display"""
        return self.choice_text
    
    def get_percentage(self):
        """
        Calculates the percentage of votes this choice received.
        Returns 0 if no votes exist yet.
        """
        total = self.poll.get_total_votes()
        if total == 0:
            return 0
        return round((self.votes / total) * 100, 1)
