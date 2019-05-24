using System.Windows;

namespace SampleWpfApplication.Views
{
    /// <summary>
    /// Interaction logic for SubWindow.xaml
    /// </summary>
    public partial class SubWindow : Window
    {
        public MainWindow Main;
        public bool IsClosing { get; set; }

        public SubWindow()
        {
            InitializeComponent();
            IsClosing = false;
        }

        public SubWindow(MainWindow main)
        {
            InitializeComponent();
            Main = main;
        }

        private void PreviousButton_Click(object sender, RoutedEventArgs e)
        {
            this.Hide();
            Main.Show();
        }

        private void SubWindow1_Closing(object sender, System.EventArgs e)
        {
            IsClosing = true;

            if (!Main.IsClosing)
            {
                Main.Close();
            }
        }
    }
}
