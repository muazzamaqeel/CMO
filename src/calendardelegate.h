#ifndef CALENDARDELEGATE_H
#define CALENDARDELEGATE_H

#include <QStyledItemDelegate>
#include <QList>
#include <QDate>

// Structure to define special dates
struct SpecialDate {
    QDate date;
    QColor backgroundColor;
    QColor textColor;
    QColor borderColor; // Added border color for special dates
};

class CalendarDelegate : public QStyledItemDelegate {
    Q_OBJECT
public:
    explicit CalendarDelegate(const QList<SpecialDate> &specialDates, QObject *parent = nullptr);

protected:
    void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override;

private:
    QList<SpecialDate> specialDates;
};

#endif // CALENDARDELEGATE_H
