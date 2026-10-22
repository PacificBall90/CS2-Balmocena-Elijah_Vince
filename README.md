# Electricity Calculator

## This python program calculates how much electricity was used and how much the bill will cost.

## Version I. Without Input Validation
- **Input**: *Accepts* a **name** along with the **original reading** of the meter and the **final reading** of the meter.
- **Process**: *Calculates* the **total electricity consumption**, and then *multiplies* it by the **rate**.
- **Output**: *Prints* the **name**, **total electricity consumption**, and the **cost** of the bill.
- Does ***not*** include **input validation**.

## Version II. With Input Validation
- **Input**:
    1. **Name**: *Checks* if **name** has a **value**, if not *prints* an **error message** and makes the user *input* again.
    2. **Original Reading**: *Checks* if the **original reading** is a **non-negative number**, if not *prints* an **error message** and makes the user *input* again.
    3. **Final Reading**: *Checks* if the **final reading** is *greater than or equal to* the **original reading**, if not *prints* an **error message** and makes the user *input* again.
- **Process**: *Calculates* the **total electricity consumption**, and then *multiplies* it by the **rate**.
- **Output**: *Prints* the **name**, **total electricity consumption**, and the **cost** of the bill.
- ***Does*** include **input validation**.
