```csharp
namespace Project.Domain.Brands
{
    public class Brand : Entity<string>
    {
        private bool _isModified = false;
        
        public Brand() { /* Needed by EF */ }
        
        private Brand(
            string id,
            string organizationId,
            Organization organization,
            Guid categoryId,
            Category category,
            string name,
            string? title,
            DateTimeOffset createdAt,
            DateTimeOffset updatedAt)
        {
            Id = id;
            OrganizationId = organizationId;
            Organization = organization;
            CategoryId = categoryId;
            Category = category;
            Name = name;
            Title = title;
            CreatedAt = createdAt;
            UpdatedAt = updatedAt;

            AddDomainEvent(new BrandCreatedEvent(this));
        }

        public static Brand Create(
            string id,
            Organization organization,
            Category category,
            string name,
            string? title,
            IBrandUniquenessChecker brandUniquenessChecker)
        {
            CheckRule(new BrandIdMustBeValidRule(brandUniquenessChecker, id, organization.Id));
            CheckRule(new StringMustNotBeEmptyRule(name, nameof(Name)));
            if (title is not null)
                CheckRule(new StringMustNotBeEmptyRule(title, nameof(Title)));

            var now = DateTimeOffset.UtcNow;

            return new Brand(
                id, 
                organization.Id,
                organization,
                category.Id,
                category,
                name, 
                title, 
                now, 
                now);
        }

        public override string Id { get; protected set; } = null!;
        public string OrganizationId { get; private set; } = null!;
        public Guid CategoryId { get; private set; }
        public string Name { get; private set; } = null!;
        public string? Title { get; private set; }
        public DateTimeOffset CreatedAt { get; private set; }
        public DateTimeOffset UpdatedAt { get; private set; }

        public virtual Organization Organization { get; private set; } = null!;
        public virtual Category Category { get; private set; } = null!;
        public virtual ICollection<BrandLocalization> Localizations { get; private set; } = Enumerable.Empty<BrandLocalization>().ToList();
        public virtual ICollection<BrandUser> Users { get; private set; } = Enumerable.Empty<BrandUser>().ToList();

        public void SetName(string name)
        {
            if (Name != name)
            {
                CheckRule(new StringMustNotBeEmptyRule(name, nameof(Name)));
                Name = name;
                _isModified = true;
            }
        }

        public void SetTitle(string? title)
        {
            if (Title != title)
            {
                if (title is not null)
                    CheckRule(new StringMustNotBeEmptyRule(title, nameof(Title)));

                Title = title;
                _isModified = true;
            }
        }

        public void SaveChanges()
        {
            if (_isModified)
            {
                UpdatedAt = DateTimeOffset.UtcNow;
                AddDomainEvent(new BrandUpdatedEvent(this));
                _isModified = false;
            }
        }

        public void Delete()
        {
            AddDomainEvent(new BrandDeletedEvent(this));
        }
    }
}
```