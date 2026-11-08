"""Render historical OECD comparisons and current regression charts separately."""
from pathlib import Path
import json
import textwrap
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]


def build(root=ROOT):
    dest=root/'outputs/stackoverflow2025/figures';dest.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.spines.left':False})
    sector=pd.read_csv(root/'results/sector_comparisons.csv').set_index('metric')
    sizes=pd.read_csv(root/'results/adoption_by_firm_size.csv').set_index('metric')
    historical=[
      ('oecd_adoption','Earlier OECD AI adoption',sizes,[('20-49 employees','20–49 employees'),('50-249 employees','50–249 employees'),('250-499 employees','250–499 employees'),('500+ employees','500+ employees')], 'All employers in each size band; original fieldwork 2022. Figure 2.1.'),
      ('oecd_performance','Earlier OECD performance perceptions',sector,[('Employer AI adoption','AI adoption'),('Employer perceived productivity: positive','Positive employer productivity perception'),('Worker perceived performance: improved','Worker performance improved')], 'Adoption: all employers; productivity: AI-adopting employers; performance: AI-using workers. Figures 2.1, 3.2, 3.3.'),
      ('oecd_work','Earlier OECD work changes',sector,[('Task automation','Task automation'),('Task creation','Task creation'),('Worker task pace: increased','Task pace increased'),('Worker task control: increased','Task control increased')], 'Tasks: AI-adopting employers; pace/control: AI-using workers. Overlapping items. Figures 5.1, 5.6.'),
      ('oecd_decisions','Earlier OECD decision assistance',sector,[('Workers receiving decision assistance','Receiving decision assistance'),('Decision quality: agreement','Better decision quality'),('Decision enjoyment: agreement','Greater decision enjoyment'),('Decision speed: agreement','Faster decisions')], 'Assistance: AI-using workers; agreement ratings: assisted workers only. Figures 5.8, 5.9.'),
      ('oecd_barriers','Earlier OECD implementation barriers',sector,[('High-cost barrier','High cost'),('Skills barrier','Skills shortage'),('Not convinced of benefits','Not convinced of benefits'),('Government-regulation barrier','Government regulation')], 'All employers; reported barriers can overlap. Figure 8.7. The excluded 94% cost-motivation item is not used.')]
    for filename,title,frame,items,note in historical:
        fig,ax=plt.subplots(figsize=(11,4.7));y=np.arange(len(items));height=.31
        for off,col,label,color in [(-height/2,'finance_percent','Finance and insurance','#2B6DAE'),(height/2,'manufacturing_percent','Manufacturing','#178D94')]:
            values=[float(frame.loc[key,col]) for key,_ in items]
            bars=ax.barh(y+off,values,height,color=color,label=label)
            ax.bar_label(bars,labels=[f'{v:.1f}%' for v in values],padding=4,fontsize=11)
        ax.set_yticks(y,['\n'.join(textwrap.wrap(label,28)) for _,label in items]);ax.invert_yaxis()
        ax.set_xlim(0,105);ax.set_xlabel('Published weighted percentage');ax.set_title(title,loc='left',fontweight='bold',pad=35)
        ax.legend(loc='lower left',bbox_to_anchor=(0,1.01),ncol=2,frameon=False)
        fig.subplots_adjust(left=.29,right=.95,top=.78,bottom=.23)
        fig.text(.025,.055,'\n'.join(textwrap.wrap('Source: Lane, Williams & Broecke (2023), OECD supplementary workbook. '+note,135)),fontsize=9,color='#536479')
        fig.savefig(dest/(filename+'.png'),dpi=180);plt.close(fig)
    data=json.loads((root/'outputs/stackoverflow2025/analysis.json').read_text(encoding='utf-8'))
    models=data['models']; labels=['Adoption: 20+ vs <5 years experience','Productivity: daily vs monthly agent use',
        'Debugging: daily vs monthly AI-tool use','Complex tasks: daily vs monthly AI-tool use','Trust: daily vs monthly AI-tool use']
    fig,ax=plt.subplots(figsize=(11.4,5.1))
    for i,m in enumerate(models):
        r=m['primary'];ax.errorbar(r['odds_ratio'],i,xerr=[[r['odds_ratio']-r['ci_low']],[r['ci_high']-r['odds_ratio']]],fmt='o',color='#178D94',capsize=5,markersize=8)
        ax.text(16,i,f'{r["odds_ratio"]:.2f}  [{r["ci_low"]:.2f}, {r["ci_high"]:.2f}]',va='center',fontsize=11)
    ax.axvline(1,color='#8A9098',linestyle='--');ax.set_xscale('log');ax.set_xlim(.35,35)
    ax.set_xticks([.5,1,2,4,8,16],['0.5','1','2','4','8','16'])
    ax.set_yticks(range(5),labels);ax.invert_yaxis();ax.set_xlabel('Adjusted odds ratio on log scale; dashed line = 1')
    ax.set_title('New Stack Overflow regression results',loc='left',fontweight='bold',pad=20)
    fig.subplots_adjust(left=.36,right=.98,bottom=.23,top=.86)
    fig.text(.025,.06,'Pointwise 95% HC1 confidence intervals. Adjusted for experience, employer size and grouped country.\nDifferent eligible samples by model. Associations in self-reported data; no causal productivity claim.',fontsize=10,color='#536479')
    fig.savefig(dest/'regression_odds_ratios.png',dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(11,4.7))
    bars=ax.barh(['Adoption','Agent productivity','Debugging frustration','Complex-task rating','Trust'],[m['n'] for m in models],color='#2B6DAE')
    ax.bar_label(bars,labels=[f'{m["n"]:,}' for m in models],padding=5)
    ax.set_xlim(0,24000);ax.invert_yaxis();ax.set_xlabel('Genuine records in each complete-case model')
    ax.set_title('New regression model sample sizes',loc='left',fontweight='bold',pad=20)
    fig.subplots_adjust(left=.23,bottom=.24,right=.96,top=.87)
    fig.text(.025,.065,'Question eligibility and missingness differ. These are overlapping analytical samples, not sequential exclusions.\nSource archive: 49,191 records; published analysis headline: 49,009. Difference of 182 remains unresolved.',fontsize=10,color='#536479')
    fig.savefig(dest/'regression_sample_sizes.png',dpi=180);plt.close(fig)
    return dest


if __name__=='__main__':print(build())
