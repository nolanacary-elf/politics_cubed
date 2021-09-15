# Creating a basic political profile and showing results of data.
import matplotlib.pyplot as plt
from matplotlib import ticker


# Create basic data structures.
# Sub-groups.
primary_sub_group = []

# For Governing Systems.
governing_systems = ['Democracy = 1', 'Mixocracy = 2', 'Autocracy = 3']
preferred_governing_system = ['Democracy', 'Mixocracy', 'Autocracy']
governing_results = []
preferred_governing_results = {}
governing_questions_answers = {
    'As a general rule, which governing system do you prefer?': governing_systems,
    'When considering race and ethnicity, which statement best reflects your'
    'beliefs': ['1 = All races and ethnic groups should have equal rights to vote.',
                '2 = All races and ethnic groups are equal, but in certain cases,'
                'one race should have more rights to restrict other races from voting.',
                '3 = Certain races and ethnic groups should not be allowed to vote.'],
    'In terms of gender, which statement do you most agree with?':
    ['1 = Both men and women have equal rights to vote.',
     '2 = In some cases one gender should have more rights.',
     '3 = One gender should always have more rights.'],
    'When it comes to religion, what is your opinion?':
    ['1 = All religions should be equally tolerated, and no religion or religions should '
     'have power over the government.',
     '2 = In some cases, one religion should assert control over other religions and '
     'limited control over the government.',
     '3 = One religion should institute a theocracy over the goverment and other religions.'],
    'For term limits fo appointed and elected public officials, what do you think?':
    ['1 = Terms should be short and no more than four terms.',
     '2 = Terms should be short but unlimited number of terms allowed.',
     '3 = No limits on term, either number of terms or duration of terms.'],
    'On inherited titles and positions in government, which alligns with your beliefs?':
    ['1 = No government positions or titles allowed.',
     '2 = Titles and positions can be inherited, but only with limited powers.',
     '3= Leaders can pass control of the government to their heirs.'],
    'When considering appointed officials, which do you agree?':
    ['1 = All government officials should be elected, no appointed officials.',
     '2 = Some officials can be appointed rather than elected.',
     '3 = All officials that do not inherit their positions should be appointed.'],
    'Voting rights should:':
    ['1 = Ensure the greatest number of people can vote.',
     '2 = Limit certian  people from voting.',
     '3 = Ensure only a small group of people control the vote.'],
    'On the amount of power granted to government officials':
    ['1 = Government officials should have specific and limited powers only.',
     '2 = Government officials can have broad and extensive powers in certain cases.',
     '3 = Government officials should have absolute power.'],
    'What power should citizens retain?':
    ['1 = Citizens should have the power to easily revoke the powers of government officials '
     'who are incompetent, corrupt, or exceed the limits of their powers.',
     '2 = Citizens can revoke the powers of government officials but it should be difficult to do so.',
     '3 = Citizens cannot revoke the powers of government officials for any reason.']
    }

# For Political Disposition.
political_dispositions = ['Open = 1', 'Partially Open = 2', 'Closed = 3']
primary_political_disposition = ['Open', 'Partailly Open', 'Closed']
disposition_results = []
dispositions_questions_answers = {
    'What is your general political disposition?': political_dispositions,
    'Are you open to new political ideas?':
    ['1 = Always.',
     '2 = Sometimes.',
     '3 = Never.'],
    'Are you willing to change your position on issues?':
    ['1 = Yes, if I think the evidence supports a change.',
     '2 = Maybe, if the evidence is strong enough.',
     '3 = No; once I make up my mind, I will not change my position for any reason.'],
    'Are you willing to compromise on issues?':
    ['1 = Yes, I can accept compromises on most or all issues.',
     '2 = Yes, but only on certain issues.',
     '3 = No to all compromises.'],
    'Can you accept that you might be wrong on an issue?':
    ['1 = Yes, no one is always correct.',
     '2 = Yes, but only on certain issues. I am generally correct.',
     '3 = No, I am certain about everything.'],
    'Do you think political issues can be solved in more than one way?':
    ['1 = Yes. Two or more solutions may exist on many issues.',
     '2 = Yes, but only on certain issues.',
     '3 = No. There can only be one single solution to any problem.'],
    'What percent of issues are you willing to consider new ideas and/or compromise on?':
    ['1 = 50% or more.',
     '2 = Up to 50%.',
     '3 = 0%'],
    'Are there any issues you are unwilling to consider new evidence that may change your mind?':
    ['1 = No',
     '2 = A few.',
     '3 = Yes. No evidence can change my position.']
    }

# For Positions on Issues.
position_on_issues = ['LL = 1', 'CL = 2', 'RL = 3',
                      'LC = 4', 'CC = 5', 'RC = 6',
                      'LR = 7', 'CR = 8', 'RR = 9']
dominant_position = ['Ultra Liberal', 'Liberal', 'Moderate Liberal',
    'Liberal Centrist', 'Centrist', 'Conservative Centrist',
    'Moderate Conservative', 'Conservative', 'Ultra Conservative']
position_results = []
issue_questions_answers = {
    'In general, how do you self-identify politically?':
    ['1 = Ultra-liberal', '2 = Liberal','3 = Moderate Liberal',
     '4 = Liberal Centrist','5 = Centrist', '6 = Conservative Centrist',
     '7 = Moderate Conservative', '8 = Conservative', '9 = Ultra Conservative'],
    'How do you most identify on social issues?':
    ['1 = Ultra-liberal', '2 = Liberal','3 = Moderate Liberal',
     '4 = Liberal Centrist','5 = Centrist', '6 = Conservative Centrist',
     '7 = Moderate Conservative', '8 = Conservative', '9 = Ultra Conservative'],
    'How do you most identify on economic issues?':
    ['1 = Ultra-liberal', '2 = Liberal','3 = Moderate Liberal',
     '4 = Liberal Centrist','5 = Centrist', '6 = Conservative Centrist',
     '7 = Moderate Conservative', '8 = Conservative', '9 = Ultra Conservative'],
    'How do you most identify on foreign policy issues?':
    ['1 = Ultra-liberal', '2 = Liberal','3 = Moderate Liberal',
     '4 = Liberal Centrist','5 = Centrist', '6 = Conservative Centrist',
     '7 = Moderate Conservative', '8 = Conservative', '9 = Ultra Conservative'],
    'What is your position on trade related issues in general?':
    ['1 = Support free trade.',
     '2 = Support free trade only with allied nations and limited free trade '
     'with non-allied nations.',
     '4 = Support limited free trade with allied nations and restricted trade '
     'with non-allied nations.',
     '5 = Support limited free trade only with certain allies, restrictive '
     'trade with the remaining allies, and no trade with non-allied nations.',
     '6 = Support only restricted trade with all allies and no trade with '
     'non-allied nations.',
     '8 = Support only restricted trade with certain allies but no trade with '
     'others.',
     '9 = Do not  support trade with others.'],
    'In your opinion, people who cannot afford medical treatment should:':
    ['1 = Recieve whatever care they need, including extensive long-term care if needed.',
     '2 = Recieve whatever care they need up to long-term care, but options for certain care may be limited to lower cost options.',
     '3 = Recieve whatever care needed up to long-term care, but some treatments (lower or higher cost) may not be available.',
     '4 = Recieve most care required and general long-term care.',
     '5 = Recieve most care required with limited long-term care.',
     '6 = Recieve most care required with limited short-term care.',
     '7 = Recieve emergency care required with limited short term care possible but not guaranteed.',
     '8 = Recieve only emergency care required.',
     '9 = No treatment given.'],
    'What do you think about safety training for gun purchases?':
    ['1 = All gun purchases should show gun buyer has completed extensive safety training that is updated annually.',
     '2 = All gun purchases should show gun buyer has completed extensive safety training that is updated bi-annually.',
     '3 = All gun purchases should show gun buyer has completed extensive safety training that is updated every 3-5 years.',
     '4 = All gun purchases should show gun buyer has completed moderate safety training that is updated annually or bi-annually.',
     '5 = All gun purchases should show gun buyer has completed moderate safety training that is updated every 3-5 years.',
     '6 = All gun purchases should show gun buyer has completed basic safety training that is updated at least every 3 years.',
     '7 = All gun purchases should show gun buyer has completed basic safety training that is updated every 5-10 years.',
     '8 = All gun purchases should show gun buyer has completed basic safety training. No updated training required.',
     '9 = No safety training should be required to own or use a gun.'],
    }

# Determine Preferred Governing System.
print('Answer the following ten questions to clarify your "Preferred Governing System."')
print('\n')

question = 1
for k, v in governing_questions_answers.items():
    print(f'Question {question}')
    print(k)
    print(f'\nChoose one:')
    for i in v:
        print(f'\t{i}')
        
    result = input('\nEnter 1, 2, 3 or (q to quit): ')
    if result == 'q':
        break
    else:
        governing_results.append(int(result))
        print('\n')
        question += 1

# Show results of Preferred Governing System.
        
if sum(governing_results) == 0:
    print('You ended your session early.')
else:
    print(governing_results)
    print('Your answers were:')
    for result in governing_results:
        if result == 1:
            print('\tDemocracy')
        elif result == 2:
            print('\tMixocracy')
        else:
            print('\tAutocracy')

    preferred_governing_system_score = sum(governing_results)/len(governing_results)
    if float(preferred_governing_system_score) == 1.0:
        print(f'Your preferred governing system is {preferred_governing_system[0]}')
        primary_sub_group.insert(1, 0.5)
        p_g_s = preferred_governing_system[0]
    elif float(preferred_governing_system_score) == 3.0:
        print(f'Your preferred governing system is {preferred_governing_system[2]}')
        primary_sub_group.insert(1, 2.5)
        p_g_s = preferred_governing_system[2]
    else:
        print(f'Your preferred governing system is {preferred_governing_system[1]}')
        primary_sub_group.insert(1, 1.5)
        p_g_s = preferred_governing_system[1]

    # Show results of Preferred Governing Systems in a pie chart.
    
    democracy_size = []
    mixocracy_size = []
    autocracy_size = []
    for result in governing_results:
        if result == 1:
            democracy_size.append(result)
        elif result == 2:
            mixocracy_size.append(result)
        elif result == 3:
            autocracy_size.append(result)

    d = len(democracy_size)
    m = len(mixocracy_size)
    a = len(autocracy_size)
    if d and m and a > 0:
        sizes = [d, m, a]
        labels = 'Democracy', 'Mixocracy', 'Autocracy'
        
        
    elif d and m > 0 and a < 1:
        sizes = [d, m]
        labels = 'Democracy', 'Mixocracy'
    elif d and a > 0 and m < 1:
        sizes = [d, a]
        labels = 'Democracy', 'Autocracy'
    elif m and a > 0 and d < 1:
        sizes = [m, a]
        labels = 'Mixocracy', 'Autocracy'
    elif a == len(governing_results):
        sizes = [a]
        labels = 'Autocracy',
    elif m == len(governing_results):
        sizes = [m]
        labels = 'Mixocracy',
        
    elif d == len(governing_results):
        sizes = [d]
        labels = 'Democracy',
       

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    ax.axis('equal')
    plt.show()

# Determine Political Disposition.
print('Answer the following ten questions to clarify your "Preferred Governing System."')
print('\n')

question = 1
for k, v in dispositions_questions_answers.items():
    print(f'Question {question}')
    print(k)
    print(f'\nChoose one:')
    for i in v:
        print(f'\t{i}')
        
    result = input('\nEnter 1, 2, 3 or (q to quit): ')
    if result == 'q':
        break
    else:
        disposition_results.append(int(result))
        print('\n')
        question += 1

# Show results of Political Disposition.

if sum(disposition_results) == 0:
    print('You ended your session early.')
else:
    print(disposition_results)
    print('Your answers were:')
    for result in disposition_results:
        if result == 1:
            print('\tOpen')
        elif result == 2:
            print('\tPartially Open')
        else:
            print('\tClosed')

    primary_disposition_score = sum(disposition_results)/len(disposition_results)
    if float(primary_disposition_score) == 1.0:
        print(f'Your primary political disposition is {primary_political_disposition[0]}')
        p_p_d = primary_political_disposition[0]
        primary_sub_group.insert(2, 0.5)
    elif float(primary_disposition_score) == 3.0:
        print(f'Your primary political disposition is {primary_political_disposition[2]}')
        primary_sub_group.insert(2, 2.5)
        p_p_d = primary_political_disposition[2]
    else:
        print(f'Your primary political disposition is {primary_political_disposition[1]}')
        primary_sub_group.insert(2, 1.5)
        p_p_d = primary_political_disposition[1]
        

        # Plot results of Political Disposition in chart(s).
    open_size = []
    partially_open_size = []
    closed_size = []
    for result in disposition_results:
        if result == 1:
            open_size.append(result)
        elif result == 2:
            partially_open_size.append(result)
        elif result == 3:
            closed_size.append(result)

    o = len(open_size)
    p = len(partially_open_size)
    c = len(closed_size)
    if o and p and c > 0:
        sizes = [o, p, c]
        labels = 'Open', 'Partially Open', 'Closed'
        
        
    elif o and p > 0 and c < 1:
        sizes = [o, p]
        labels = 'Open', 'Partially Open'
    elif o and c > 0 and p < 1:
        sizes = [o, c]
        labels = 'Open', 'Closed'
    elif m and a > 0 and d < 1:
        sizes = [p, c]
        labels = 'Partially Open', 'Closed'
    elif o == len(disposition_results):
        sizes = [o]
        labels = 'Open',
    elif p == len(disposition_results):
        sizes = [p]
        labels = 'Partially Open',
        
    elif c == len(disposition_results):
        sizes = [c]
        labels = 'Closed',
       

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    ax.axis('equal')
    plt.show()

# Determine positions on issues..
print('Answer the following questions to clarify your "Positions on Issues."')
print('\n')

question = 1
for k, v in issue_questions_answers.items():
    print(f'Question {question}')
    print(k)
    print(f'\nChoose one:')
    for i in v:
        print(f'\t{i}')
        
    result = input('\nEnter number of choice (examples: 1, 2, 3, 4, 5, 6, 7, 8, or 9). or (q to quit): ')
    if result == 'q':
        break
    else:
        position_results.append(int(result))
        print('\n')
        question += 1

# Show results of Position on Issues.
        
if sum(position_results) == 0:
    print('You ended your session early.')
else:
    print(position_results)
    print('Your answers were:')
    for result in position_results:
        if result == 1:
            print('\tLeft leaning Left')
        elif result == 2:
            print('\tCenter Left')
        elif result == 3:
            print('\tRight leaning Left')
        elif result == 4:
            print ('\tLeft leaning Center')
        elif result == 5:
            print('\tCenter of Center')
        elif result == 6:
            print('\tRight leaning Center')
        elif result == 7:
            print('\tLeft leaning Right')
        elif result == 8:
            print('\tCenter Right')
        else:
            print('\tRight leaning Right')

    position_score = sum(position_results)/len(position_results)
    if float(position_score) < 2.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[0]}')
        primary_sub_group.insert(0, 0.5)
        d_p = dominant_position[0]
    elif float(position_score) < 3.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[1]}')
        primary_sub_group.insert(0, 1.5)
        d_p = dominant_position[1]
    elif float(position_score) < 4.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[2]}')
        primary_sub_group.insert(0, 2.5)
        d_p = dominant_position[2]
    elif float(position_score) < 5.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[3]}')
        primary_sub_group.insert(0, 3.5)
        d_p = dominant_position[3]
    elif float(position_score) < 6.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[4]}')
        primary_sub_group.insert(0, 4.5)
        d_p = dominant_position[4]
    elif float(position_score) < 7.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[5]}')
        primary_sub_group.insert(0, 5.5)
        d_p = dominant_position[5]
    elif float(position_score) < 8.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[6]}')
        primary_sub_group.insert(0, 6.5)
        d_p = dominant_position[6]
    elif float(position_score) < 9.0:
        print(f'Your dominant position on questions answered so far is {dominant_position[7]}')
        primary_sub_group.insert(0, 7.5)
        d_p = dominant_position[7]
    else:
        print(f'Your dominant position on questions answered so far is {dominant_position[8]}')
        primary_sub_group.insert(0, 8.5)
        d_p = dominant_position[8]

    # Show results of Position on Issues in a pie chart.
    
    ll_size = []
    cl_size = []
    rl_size = []
    lc_size = []
    cc_size = []
    rc_size = []
    lr_size = []
    cr_size = []
    rr_size = []
    for result in position_results:
        if result == 1:
            ll_size.append(result)
        elif result == 2:
            cl_size.append(result)
        elif result == 3:
            rl_size.append(result)
        elif result == 4:
            lc_size.append(result)
        elif result == 5:
            cc_size.append(result)
        elif result == 6:
            rc_size.append(result)
        elif result == 7:
            lr_size.append(result)
        elif result == 8:
            cr_size.append(result)
        elif result == 9:
            rr_size.append(result)

    sizes = []
    labels_list = []
    ll = len(ll_size)
    if ll > 0:
        sizes.append(ll)
        labels_list.append('Left leaning Left')
    cl = len(cl_size)
    if cl > 0:
        sizes.append(cl)
        labels_list.append('Center Left')
    rl = len(rl_size)
    if rl > 0:
        sizes.append(rl)
        labels_list.append('Right leaning Left')
    lc = len(lc_size)
    if lc > 0:
        sizes.append(lc)
        labels_list.append('Left of Center')
    cc = len(cc_size)
    if cc > 0:
        sizes.append(cc)
        labels_list.append('Center of Center')
    rc = len(rc_size)
    if rc > 0:
        sizes.append(rc)
        labels_list.append('Right of Center')
    lr = len(lr_size)
    if lr > 0:
        sizes.append(lr)
        labels_list.append('Left leaning Right')
    cr = len(cr_size)
    if cr > 0:
        sizes.append(cr)
        labels_list.append('Center Right')
    rr = len(rr_size)
    if rr > 0:
        sizes.append(rr)
        labels_list.append('Right leaning Right')
        
       

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels_list)
    ax.axis('equal')
    plt.show()

# Show results of Sub-groups.
    print('\n\n\n')
    print(f'According to your answers, the Political Sub-group you most identify with is a '
          f'{d_p} who prefers {p_g_s} as the government type and, typically, you are {p_p_d} '
          f'to new political ideas or compromises.')
    
    print('\nThis is a 3d visualization of the 81 Political Sub-groups with you primary Sub-group plotted as an orange dot.')
    left_issue_values = [0.5, 1.5, 2.5]
    center_issue_values = [3.5, 4.5, 5.5]
    right_issue_values = [6.5, 7.5, 8.5]
    governing_system_values = [0.5, 1.5, 2.5]
    political_openness_values = [0.5, 1.5, 2.5]

    #plt.style.use('classic')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('Issue Position', c='green')
    #ax.set_ylabel('Governing System', c='green')
    #ax.set_zlabel('Political Openness', c='green')
    fig.suptitle('Politics Cubed', fontsize=14, fontweight='bold')
    ax.set_title('81 Political Sub-groups', c='brown')

    for l in left_issue_values: # Plots all Political Sub-groups on left.
        ax.scatter(l, 0.5, 0.5, c='blue')
        ax.scatter(l, 0.5, 1.5, c='blue')
        ax.scatter(l, 0.5, 2.5, c='blue')
        ax.scatter(l, 1.5, 0.5, c='blue')
        ax.scatter(l, 1.5, 1.5, c='blue')
        ax.scatter(l, 1.5, 2.5, c='blue')
        ax.scatter(l, 2.5, 0.5, c='blue')
        ax.scatter(l, 2.5, 1.5, c='blue')
        ax.scatter(l, 2.5, 2.5, c='blue')

    for c in center_issue_values: # Plots Sub-groups in center.
        ax.scatter(c, 0.5, 0.5, c='m')
        ax.scatter(c, 0.5, 1.5, c='m')
        ax.scatter(c, 0.5, 2.5, c='m')
        ax.scatter(c, 1.5, 0.5, c='m')
        ax.scatter(c, 1.5, 1.5, c='m')
        ax.scatter(c, 1.5, 2.5, c='m')
        ax.scatter(c, 2.5, 0.5, c='m')
        ax.scatter(c, 2.5, 1.5, c='m')
        ax.scatter(c, 2.5, 2.5, c='m')

    for r in right_issue_values: # Plots Sub-groups on right.
        ax.scatter(r, 0.5, 0.5, c='red')
        ax.scatter(r, 0.5, 1.5, c='red')
        ax.scatter(r, 0.5, 2.5, c='red')
        ax.scatter(r, 1.5, 0.5, c='red')
        ax.scatter(r, 1.5, 1.5, c='red')
        ax.scatter(r, 1.5, 2.5, c='red')
        ax.scatter(r, 2.5, 0.5, c='red')
        ax.scatter(r, 2.5, 1.5, c='red')
        ax.scatter(r, 2.5, 2.5, c='red')
    
    ax.plot([0, 9], [0, 0], [0, 0], zdir='z', c='black')
    ax.plot([0, 9], [3, 3], [0, 0], zdir='z', c='black')
    ax.plot([0, 0], [0, 3], [0, 0], zdir='z', c='black')
    ax.plot([9, 9], [0, 3], [0, 0], zdir='z', c='black')
    ax.plot([0, 9], [0, 0], [3, 3], zdir='z', c='black')
    ax.plot([0, 9], [3, 3], [3, 3], zdir='z', c='black')
    ax.plot([0, 0], [0, 3], [3, 3], zdir='z', c='black')
    ax.plot([9, 9], [0, 3], [3, 3], zdir='z', c='black')
    ax.plot([0, 0], [0, 0], [0, 3], zdir='z', c='black')
    ax.plot([0, 0], [3, 3], [0, 3], zdir='z', c='black')
    ax.plot([9, 9], [0, 0], [0, 3], zdir='z', c='black')
    ax.plot([9, 9], [3, 3], [0, 3], zdir='z', c='black')

    

    ax.scatter(primary_sub_group[0], primary_sub_group[2], primary_sub_group[1], c='orange', s=200) # Highlights a specific Sub-group.

    # Customizing ticks.
    y_positions = [1, 2, 3]
    governing_systems = ['Democracy', 'Mixocracy', 'Autocracy']
    ax.yaxis.set_major_locator(ticker.FixedLocator(y_positions))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(governing_systems))

    z_positions = [0, 1, 2]
    political_openness = ['Open', 'Partial Open', 'Closed']
    ax.zaxis.set_major_locator(ticker.FixedLocator(z_positions))
    ax.zaxis.set_major_formatter(ticker.FixedFormatter(political_openness))

    fig.tight_layout()

    plt.show()
# Plot results of Sub-groups.

    
    
                                                        
                
    
          
