using System;
using System.Windows;

namespace SampleWpfApplication.Views
{
    /// <summary>
    /// Interaction logic for Dialog1.xaml
    /// </summary>
    public partial class RegisterDialog : Window
    {
        public RegisterDialog()
        {
            InitializeComponent();
        }

        private void RegisterDialogButton_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
        public string CustomerName
        {
            get { return CustomerNameTextBox.Text; }
        }
        public string CustomerBirthday
        {
            get { return CustomerBirthdayTextBox.Text; }
        }
        private void Window_ContentRendered(object sender, EventArgs e)
        {
            CustomerNameTextBox.Focus();
        }
    }
}
