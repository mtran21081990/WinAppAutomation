using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Automation.Peers;
using System.Windows.Controls;

namespace SampleWpfApplication
{
    public class LabeledComboBoxNoAutomated : Control
    {
        static LabeledComboBoxNoAutomated()
        {
            DefaultStyleKeyProperty.OverrideMetadata(typeof(LabeledComboBoxNoAutomated), new FrameworkPropertyMetadata(typeof(LabeledComboBoxNoAutomated)));
        }
        
    }
}
