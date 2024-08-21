```csharp
namespace Project.Domain.Brands.DomainEvents
{
    public class BrandDeletedEvent : DomainEventBase
    {
        public Brand Brand { get; }
        public DateTimeOffset Date { get; }

        public BrandDeletedEvent(Brand brand)
        {
            Brand = brand;
            Date = DateTimeOffset.UtcNow;
        }
    }
}
```