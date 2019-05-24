using System.Windows;

namespace SampleWpfApplication.Views
{
    /// <summary>
    /// Interaction logic for SubWindow.xaml
    /// </summary>
    public partial class SubWindow : Window
    {
        public Window Main;

        public SubWindow()
        {
            InitializeComponent();
        }

        public SubWindow(Window main)
        {
            InitializeComponent();
            Main = main;
        }

        private void PreviousButton_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
            Main.Show();
        }
    }
}
