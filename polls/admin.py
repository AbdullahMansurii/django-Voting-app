from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils import timezone
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html
from django.urls import reverse
from .models import Poll, Choice


class CustomAdminSite(AdminSite):
    """
    Custom admin site with dashboard view showing stats and quick actions.
    """
    site_header = "Voting App Admin"
    site_title = "Voting App Admin Portal"
    index_title = "Dashboard Overview"
    
    def get_urls(self):
        """
        Override to add custom dashboard view.
        """
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls
    
    def index(self, request, extra_context=None):
        """
        Override index to show custom dashboard with stats.
        """
        extra_context = extra_context or {}
        
        # Get all polls
        all_polls = Poll.objects.all()
        
        # Calculate statistics
        total_polls = all_polls.count()
        active_polls = sum(1 for poll in all_polls if poll.is_currently_active())
        past_polls = total_polls - active_polls
        
        # Get total votes across all polls
        total_votes = sum(poll.get_total_votes() for poll in all_polls)
        
        # Get total choices
        total_choices = Choice.objects.count()
        
        # Get recent polls (last 5)
        recent_polls = all_polls.order_by('-created_at')[:5]
        
        # Get polls with most votes
        polls_with_votes = [(poll, poll.get_total_votes()) for poll in all_polls]
        polls_with_votes.sort(key=lambda x: x[1], reverse=True)
        top_polls = polls_with_votes[:5]
        
        extra_context.update({
            'total_polls': total_polls,
            'active_polls': active_polls,
            'past_polls': past_polls,
            'total_votes': total_votes,
            'total_choices': total_choices,
            'recent_polls': recent_polls,
            'top_polls': top_polls,
        })
        
        return super().index(request, extra_context)
    
    def dashboard_view(self, request):
        """
        Custom dashboard view with statistics and quick actions.
        """
        # Get all polls
        all_polls = Poll.objects.all()
        
        # Calculate statistics
        total_polls = all_polls.count()
        active_polls = sum(1 for poll in all_polls if poll.is_currently_active())
        past_polls = total_polls - active_polls
        
        # Get total votes across all polls
        total_votes = sum(poll.get_total_votes() for poll in all_polls)
        
        # Get total choices
        total_choices = Choice.objects.count()
        
        # Get recent polls (last 5)
        recent_polls = all_polls.order_by('-created_at')[:5]
        
        # Get polls with most votes
        polls_with_votes = [(poll, poll.get_total_votes()) for poll in all_polls]
        polls_with_votes.sort(key=lambda x: x[1], reverse=True)
        top_polls = polls_with_votes[:5]
        
        context = {
            **self.each_context(request),
            'total_polls': total_polls,
            'active_polls': active_polls,
            'past_polls': past_polls,
            'total_votes': total_votes,
            'total_choices': total_choices,
            'recent_polls': recent_polls,
            'top_polls': top_polls,
        }
        return render(request, 'admin/dashboard.html', context)


# Create custom admin site instance
custom_admin_site = CustomAdminSite(name='custom_admin')


class ChoiceInline(admin.TabularInline):
    """
    Allows adding choices directly when creating/editing a poll in admin.
    This makes it easier to manage poll options.
    """
    model = Choice
    extra = 3  # Shows 3 empty choice fields by default
    classes = ['collapse']


@admin.register(Poll, site=custom_admin_site)
class PollAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Poll model.
    Allows managing polls with their choices in one place.
    """
    # Fields to display in the list view
    list_display = ('title', 'is_active', 'created_at', 'end_date', 'vote_count_display', 'quick_actions')
    # Fields that can be filtered
    list_filter = ('is_active', 'created_at')
    # Fields to search
    search_fields = ('title', 'question')
    # Include choices inline
    inlines = [ChoiceInline]
    # Fields shown when editing a poll
    fieldsets = [
        ('Poll Information', {'fields': ['title', 'question']}),
        ('Status', {'fields': ['is_active', 'end_date']}),
    ]
    # Order polls by creation date (newest first)
    ordering = ('-created_at',)
    
    def vote_count_display(self, obj):
        """
        Display total votes for this poll in a styled format.
        """
        count = obj.get_total_votes()
        color = 'green' if count > 0 else 'gray'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            count
        )
    vote_count_display.short_description = 'Total Votes'
    
    def quick_actions(self, obj):
        """
        Quick action buttons for each poll.
        """
        view_url = reverse('custom_admin:polls_poll_change', args=[obj.pk])
        return format_html(
            '<a href="{}" class="button" style="background: linear-gradient(135deg, #667eea, #764ba2) !important; color: #ffffff !important; padding: 5px 10px; border-radius: 4px; text-decoration: none; margin-right: 5px; font-weight: 600;">Edit</a>',
            view_url
        )
    quick_actions.short_description = 'Actions'


@admin.register(Choice, site=custom_admin_site)
class ChoiceAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Choice model.
    Shows choices with their vote counts.
    """
    list_display = ('choice_text', 'poll', 'votes', 'percentage_display')
    list_filter = ('poll',)
    search_fields = ('choice_text',)
    ordering = ('-votes',)
    
    def percentage_display(self, obj):
        """
        Display vote percentage with visual bar.
        """
        percentage = obj.get_percentage()
        return format_html(
            '<div style="display: flex; align-items: center; gap: 10px;">'
            '<div style="width: 100px; height: 8px; background: #2d3748; border-radius: 4px; overflow: hidden;">'
            '<div style="width: {}%; height: 100%; background: linear-gradient(90deg, #667eea, #764ba2);"></div>'
            '</div>'
            '<span style="font-weight: bold;">{}%</span>'
            '</div>',
            percentage,
            percentage
        )
    percentage_display.short_description = 'Vote %'
