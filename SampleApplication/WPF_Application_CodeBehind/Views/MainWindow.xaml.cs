using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Globalization;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace SampleWpfApplication.Views
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public Window Sub;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void MainPageWindow_Loaded(object sender, RoutedEventArgs e)
        {
            //this.WindowState = System.Windows.WindowState.Maximized;
            this.Activate();
        }

        private void AvailableDateCalendar_SelectedDatesChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
        {
            AvailableDateTextBox.Text = AvailableDateCalendar.SelectedDate.ToString();
        }

        private void WindowColorMenuItem_Click(object sender, RoutedEventArgs e)
        {
            MenuItem itm = (MenuItem) sender;
            switch(itm.Header.ToString())
            {
                case "Yellow":
                    MainPageWindow.Background = Brushes.Yellow;
                    MainPageGrid.Background = Brushes.Yellow;
                    break;
                case "Orange": MainPageWindow.Background = Brushes.Orange;
                    MainPageGrid.Background = Brushes.Orange;
                    break;
                case "Red": MainPageWindow.Background = Brushes.Red;
                    MainPageGrid.Background = Brushes.Red;
                    break;
                default: MainPageWindow.Background = Brushes.White;
                    MainPageGrid.Background = Brushes.White;
                    break;
            }
        }

        private void RegularCustomerRegisterButton_Click(object sender, RoutedEventArgs e)
        {
            RegisterDialog dialog = new RegisterDialog();
            dialog.Show();
        }

        private void DgUsers_Loaded(object sender, RoutedEventArgs e)
        {
            List<BirthdayMember> BirthdayList = new List<BirthdayMember>();
            BirthdayList.Add(new BirthdayMember() { Id = 1, Name = "John Doe", Birthday = new DateTime(1971, 7, 23) });
            BirthdayList.Add(new BirthdayMember() { Id = 2, Name = "Jane Doe", Birthday = new DateTime(1974, 1, 17) });
            BirthdayList.Add(new BirthdayMember() { Id = 3, Name = "Sammy Doe", Birthday = new DateTime(1991, 9, 2) });
            dgUsers.ItemsSource = BirthdayList;
        }

        private void DgUsers_LoadingRow(object sender, DataGridRowEventArgs e)
        {
            e.Row.Header = (e.Row.GetIndex() + 1).ToString();
        }

        private void ViewToggleButton_Click(object sender, RoutedEventArgs e)
        {
            ToggleButton tgb = (ToggleButton) sender;
            if (tgb.IsChecked.Value)
            {
                tgb.Background = new LinearGradientBrush(Colors.Black, Colors.SlateBlue, 90);
            }
            else
            {
                tgb.Background = new LinearGradientBrush(Colors.LightBlue, Colors.SlateBlue, 90);
            }
        }

        private void ViewToggleButton_Loaded(object sender, RoutedEventArgs e)
        {
            ToggleButton tgb = (ToggleButton)sender;
            tgb.Background = new LinearGradientBrush(Colors.LightBlue, Colors.SlateBlue, 90);
        }


        private void NextButton_Click(object sender, RoutedEventArgs e)
        {
            // Hide the Main window
            this.Hide();

            // Initiate and show the Sub window
            if (Sub == null)
            {
                Sub = new SubWindow(this);
            }
            Sub.Show();
        }

        private void MainPageWindow_Closing(object sender, CancelEventArgs e)
        {
            if (Sub != null)
            {
                Sub.Close();
            }
        }
    }

    public class BirthdayMember
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime Birthday { get; set; }
        public string Details
        {
            get
            {
                return String.Format("{0} was born on {1}.", this.Name, this.Birthday.ToLongDateString());
            }
            set { }
        }
    }

    public class AddNewlineConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            string original = System.Convert.ToString(value);
            return original.Replace(" ", "");
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }

    public class ImageConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            try
            {
                ComboBoxItem item = (ComboBoxItem)value;
                string text = item.Content.ToString();
                var path = string.Format(@"{0}Image\{1}.jpg", AppDomain.CurrentDomain.BaseDirectory, text);
                return new BitmapImage(new Uri(path));
            }
            catch (Exception)
            {
                return null; // or some default image
            }
        }
        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }

}
