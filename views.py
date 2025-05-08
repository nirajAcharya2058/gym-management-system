from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import timedelta
from .gym_app.models import Enrollment, Attendance, Payment, Membership, Activity

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    
    # Get statistics
    total_members = Enrollment.objects.count()
    today_attendance = Attendance.objects.filter(Selectdate__date=timezone.now().date()).count()
    monthly_revenue = Payment.objects.filter(
        date__date__month=timezone.now().month,
        date__date__year=timezone.now().year
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Get monthly attendance data for chart
    today = timezone.now().date()
    first_day = today.replace(day=1)
    last_day = (first_day + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    attendance_data = []
    for i in range((last_day - first_day).days + 1):
        date = first_day + timedelta(days=i)
        count = Attendance.objects.filter(Selectdate__date=date).count()
        attendance_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'count': count
        })
    
    # Get recent activities
    recent_activities = Activity.objects.order_by('-timestamp')[:5]
    
    # Get upcoming renewals
    upcoming_renewals = Membership.objects.filter(
        end_date__gte=today,
        end_date__lte=today + timedelta(days=30)
    ).select_related('member', 'plan')
    
    renewals = []
    for membership in upcoming_renewals:
        days_left = (membership.end_date - today).days
        renewals.append({
            'member': membership.member.username,
            'plan': membership.plan.plan,
            'days_left': days_left
        })
    
    context = {
        'total_members': total_members,
        'today_attendance': today_attendance,
        'monthly_revenue': monthly_revenue,
        'attendance_data': attendance_data,
        'recent_activities': recent_activities,
        'upcoming_renewals': renewals
    }
    
    return render(request, 'admin_dashboard.html', context) 