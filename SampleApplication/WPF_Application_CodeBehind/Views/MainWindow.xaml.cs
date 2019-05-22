using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Threading;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Data;

namespace SampleWpfApplication.Views
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            this.Title = "Sample WPF Application";
            /// Thread.Sleep(5000);
            this.WindowState = System.Windows.WindowState.Maximized;

        }

        private void Calendar_SelectedDatesChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
        {
            CalendarTextbox1.Text = Calendar1.SelectedDate.ToString();
        }

        private void DatePicker1_SelectedDateChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
        {
            DatePickerTextbox1.Text = DatePicker1.SelectedDate.ToString();
        }

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {
            MenuItem itm = (MenuItem)sender;
            if (itm.Header.ToString() == "Item 1")
            {
                MessageBox.Show("Menu Item 1 clicked");
            }
            else if (itm.Header.ToString() == "Item 3")
            {
                MessageBoxResult result = MessageBox.Show("Sample Yes No Question", "Sample Yes No Dialog", MessageBoxButton.YesNo, MessageBoxImage.Question);

            }
        }

        private void ProgressBarButton1_Click(object sender, RoutedEventArgs e)
        {
            BackgroundWorker worker = new BackgroundWorker();
            worker.WorkerReportsProgress = true;
            worker.DoWork += worker_DoWork;
            worker.ProgressChanged += worker_ProgressChanged;
            worker.RunWorkerAsync();
        }

        void worker_DoWork(object sender, DoWorkEventArgs e)
        {
            for (int i = 0; i < 100; i++)
            {
                (sender as BackgroundWorker).ReportProgress(i);
                Thread.Sleep(100);
            }
        }

        void worker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            ProgressBar1.Value = e.ProgressPercentage;
        }
        private void ProgressBar1_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            ProgressBar1.Visibility = (ProgressBar1.Value == 0 || ProgressBar1.Value == 99.0) ? Visibility.Hidden : Visibility.Visible;
        }

        private void TextBox1_MouseEnter(object sender, System.Windows.Input.MouseEventArgs e)
        {
            TextBox1.Clear();
        }

        private void TextBox2_GotFocus(object sender, RoutedEventArgs e)
        {
            TextBox2.Clear();
        }

        private void ToggleButtonPopup1_Checked(object sender, RoutedEventArgs e)
        {
            if(!Popup1.IsOpen)
                Popup1.IsOpen = true;
            else
                Popup1.IsOpen = false;
        }

        private void ButtonDialog1_Click(object sender, RoutedEventArgs e)
        {
            Dialog1 inputDialog = new Dialog1();
            inputDialog.Show();
        }

        private void ListBox1_Loaded(object sender, RoutedEventArgs e)
        {
            ListBoxItem item = (ListBoxItem) ListBox1.Items[3];
            item.IsSelected = true;
        }

        private void Lb_SampleBinding_Loaded(object sender, RoutedEventArgs e)
        {
            Dictionary<string, string> items = new Dictionary<string, string>();
            items.Add("item_1", "Binding Sample 1");
            items.Add("item_2", "Binding Sample 2");
            items.Add("item_3", "Binding Sample 3");

            List<ListBoxItem> list = new List<ListBoxItem>();

            foreach (KeyValuePair<string, string> itm in items)
            {
                AddListBoxItemWithId(list, itm.Value, itm.Key);
            }

            ICollectionView view = CollectionViewSource.GetDefaultView(list);
            lb_SampleBinding.ItemsSource = view;
        }

        private void AddListBoxItemWithId(List<ListBoxItem> list, string content, string id)
        {
            ListBoxItem newLBI = new ListBoxItem();
            newLBI.Content = content;
            newLBI.SetValue(AutomationProperties.AutomationIdProperty, id);
            list.Add(newLBI);
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
    }
    public class ListBoxItemSampleBinding
    {
        public int ItemId { get; set; }
        public string ItemContent { get; set; }
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
        
}
