#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Set up the calendar widget properties
    ui->CalendarBoard1->setMinimumDate(QDate(1900, 1, 1));
    ui->CalendarBoard1->setMaximumDate(QDate(2100, 1, 1));

    ui->CalendarBoard1->setGridVisible(true);

    // Set the window title
    setWindowTitle(tr("CMO Calendar"));
}

MainWindow::~MainWindow()
{
    delete ui;
}
