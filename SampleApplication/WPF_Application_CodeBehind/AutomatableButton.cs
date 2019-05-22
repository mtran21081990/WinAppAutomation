using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Automation.Peers;
using System.Windows.Controls;

namespace SampleWpfApplication
{
    class AutomatableButton : Button
    {
        protected override AutomationPeer OnCreateAutomationPeer()
        {
            return new AutomatableButtonAutomationPeer(this);
        }

        class AutomatableButtonAutomationPeer : ButtonAutomationPeer
        {
            public AutomatableButtonAutomationPeer(Button owner) : base(owner)
            { }

            protected override bool IsControlElementCore()
            { return true; }
        }
    }
}
