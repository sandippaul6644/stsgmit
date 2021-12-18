# Generated by Django 3.2.6 on 2021-10-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_conactno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='pin',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='active',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='academic',
            name='studentdept',
            field=models.CharField(choices=[('', 'Depertment'), ('Not Applicable', 'Not Applicable'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil '), ('Electrical', 'Electrical'), ('ComputerScience', 'Computer Science'), ('Electronics&Communication', 'Electronics & Communication')], default='Computer Science', max_length=40),
        ),
        migrations.AlterField(
            model_name='academic',
            name='studentsemester',
            field=models.CharField(choices=[('', 'Semester'), ('Not Applicable', 'Not Applicable'), ('FirstSemester', 'First Semester'), ('SecondSemester', 'Second Semester '), ('ThirdSemester', 'Third Semester'), ('FourthSemester', 'Fourth Semester'), ('FifthSemester', 'Fifth Semester'), ('SixthSemester', 'Sixth Semester'), ('SeventhSemester', 'Seventh Semester'), ('EightthSemester', 'Eightth Semester')], default='First Semester', max_length=40),
        ),
        migrations.AlterField(
            model_name='academic',
            name='studentyear',
            field=models.CharField(choices=[('', 'Year'), ('Not Applicable', 'Not Applicable'), ('FirstYear', 'First Year'), ('SecondYear', 'Second Year '), ('ThirdYear', 'Third Year'), ('FourthYear', 'Fourth Year')], default='First Year', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.CharField(choices=[('', 'Depertment'), ('Not Applicable', 'Not Applicable'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil '), ('Electrical', 'Electrical'), ('ComputerScience', 'Computer Science'), ('Electronics&Communication', 'Electronics & Communication')], default='Computer Science', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='semester',
            field=models.CharField(choices=[('', 'Semester'), ('Not Applicable', 'Not Applicable'), ('FirstSemester', 'First Semester'), ('SecondSemester', 'Second Semester '), ('ThirdSemester', 'Third Semester'), ('FourthSemester', 'Fourth Semester'), ('FifthSemester', 'Fifth Semester'), ('SixthSemester', 'Sixth Semester'), ('SeventhSemester', 'Seventh Semester'), ('EightthSemester', 'Eightth Semester')], default='First Semester', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('', 'Year'), ('Not Applicable', 'Not Applicable'), ('FirstYear', 'First Year'), ('SecondYear', 'Second Year '), ('ThirdYear', 'Third Year'), ('FourthYear', 'Fourth Year')], default='First Year', max_length=40),
        ),
    ]