#include "CalendarDelegate.h"
#include <QPainter>

CalendarDelegate::CalendarDelegate(const QList<SpecialDate> &specialDates, QObject *parent)
    : QStyledItemDelegate(parent), specialDates(specialDates) {}

void CalendarDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const {
    QDate date = index.data(Qt::UserRole + 1).toDate();

    // Custom rendering for special dates
    for (const SpecialDate &specialDate : specialDates) {
        if (date == specialDate.date) {
            painter->save();
            painter->fillRect(option.rect, specialDate.backgroundColor);
            QPen pen(specialDate.borderColor);
            pen.setWidth(2);
            painter->setPen(pen);
            painter->drawRect(option.rect.adjusted(1, 1, -1, -1));
            painter->setPen(specialDate.textColor);
            painter->restore();
            break;
        }
    }

    // Default painting for other dates
    QStyledItemDelegate::paint(painter, option, index);
}
